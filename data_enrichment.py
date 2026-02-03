"""Enrich the scraped data using Scopus."""

# The code in this file is very 'hacky': it was used to quickly acquire more data and in a few cases the output data was manually fixed / curated.
# As the resulting data did not yield great insights 'straight away', it was never brought to a more readable/repeatable level.

import csv
import yaml
from pathlib import Path

import pybliometrics
from pybliometrics.scopus import ScopusSearch
import pandas as pd


scopus_api_key = yaml.safe_load(open("api_keys.yaml"))["scopus"]
pybliometrics.init(keys=[scopus_api_key])


titles = pd.read_csv(Path("reviews.csv"))["title"].to_list()

print(f"Querying {len(titles)} titles...")

# TODO: Fix titles in unfindable.txt

enriched_output = Path("enriched_data.csv")
unfindable_output = Path("unfindable.txt")

if not enriched_output.exists():
    enriched_output.touch()

unfindable_mappings = {}

for line in unfindable_output.open().readlines():
    if "-->" in line:
        source, target = line.split(" --> ")
        unfindable_mappings[source] = target

already_done_titles = []
header_present = False
with enriched_output.open('a+', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     lines = enriched_output.open('r').readlines()
     if len(lines) > 0:
         header_present = True
     if len(lines) > 1:
        df = pd.read_csv(enriched_output)
        num_cols = len(df.columns)
        title_col = df.columns.to_list().index("title")
        cite_count_col = df.columns.to_list().index("citedby_count")
        already_done_titles = [s.lower() for s in df["title"].to_list()]

# Some little stealing from https://stackoverflow.com/questions/33404752/removing-emojis-from-a-string-in-python
def deEmojify(text):
    import re
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)

# Titles that just won't rematch with their original
bad_titles = [
    "MMVQA: A Comprehensive Dataset for Investigating Multipage Multimodal Information Retrieval in PDF-based Visual Question Answering",
    "DANETs: Deep Abstract Networks for Tabular Data Classification and Regression",
    "‘Beach’ to ‘Bitch’: Inadvertent Unsafe Transcription of Kids’ Content on YouTube",
    "FastAMI – a Monte Carlo Approach to the Adjustment for Chance in Clustering Comparison Metrics",
    "RSPT: Reconstruct Surroundings and Predict Trajectory for Generalizable Active Object Tracking",
    "“Allot?” Is “A Lot!” Towards Developing More Generalized Speech Recognition System for Accessible Communication",
    "Fair Equilibria in Sponsored Search Auctions: The Advertisers' Perspective",
    "Learning Discrete Representations via Constrained Clustering for Effective and Efficient Dense Retrieval (Extended Abstract)",
    "GS2P: A Generative Pre-trained Learning to Rank Model with Over-parameterization for Web-Scale Search (Extended Abstract)",
    "Topological Graph Neural Networks",
    "Scaling Laws for Neural Machine Translation",
    "Reversible Column Networks",
    "KWIKBUCKS: CORRELATION CLUSTERING WITH CHEAP-WEAK AND EXPENSIVE-STRONG SIGNALS",
    "QUANTIZED COMPRESSED SENSING WITH SCORE-BASED GENERATIVE MODELS",
    "Multilinear Operator Networks",
    "Mixture of LoRA Experts",
    "Never Train from Scratch: Fair Comparison of Long-Sequence Models Requires Data-Driven Priors",
    "Computing Unsatisfiable Cores for LTLf Specifications",
]

for title in titles:
    # Testing example
    #title = "Joint Human Pose Estimation and Instance Segmentation with PosePlusSeg"
    if title.lower() in already_done_titles:
        print(f"\tAlready present: {title}. Skipping.")
        continue

    try:
        if title in unfindable_mappings.keys():
            search_title = unfindable_mappings[title]
        else:
            search_title = title.replace("(Extended Abstract)", "")
        # Replace question mark, colons and exclamation as they cause issues with search
        search_title = search_title.replace("!", "").replace("?", "").replace(":", "").replace("^", "").replace(",", "")
        search_title = deEmojify(search_title)
        s = ScopusSearch(f'TITLE("{search_title}")')
    except Exception as ex:
        print(f"Exception on title: {title}")
        print(ex)
        print("Type citation count or anything else to skip: ", end="")
        c_count = input()
        try:
            c_count = int(c_count)
        except:
            continue
        t_output = ["" for _ in range(num_cols)]
        t_output[title_col] = f'"{title}"'
        t_output[cite_count_col] = str(c_count)
        with enriched_output.open("a+") as fout:
            fout.write(f"{','.join(t_output)}\n")
        continue

    if s.results is None:
        print(f"Could not find: {title}")
        print("Type citation count or anything else to skip: ", end="")
        c_count = input()
        try:
            c_count = int(c_count)
        except:
            if not unfindable_output.exists():
                unfindable_output.touch()
            with unfindable_output.open("a+") as fout:
                fout.write(f"{title}\n")
            continue
        t_output = ["" for _ in range(num_cols)]
        t_output[title_col] = f'"{title}"'
        t_output[cite_count_col] = str(c_count)
        with enriched_output.open("a+") as fout:
            fout.write(f"{','.join(t_output)}\n")
        continue

    if len(s.results) > 1:
        if title in bad_titles:
            continue
        print(f"Multiple results for: {title}")
        option_list = [{name: item for name, item in zip(option._fields, option)}
                       for option in s.results]
        for index, option in enumerate(option_list):
            print(f"\t[{index}] {option['title']}")
        print("Select the index which matches best, or s to skip: ", end="")
        selection = input()
        if selection == "s":
            with unfindable_output.open("a+") as fout:
                fout.write(f"{title}\n")
            print("Skipping..")
            continue
        selection = int(selection)
        paper_meta = option_list[selection]
    else:
        paper_meta = s.results[0]
        paper_meta = {name: item for name, item in zip(paper_meta._fields, paper_meta)}

    if paper_meta["title"] in already_done_titles:
        print(f"Already wrote: {paper_meta["title"]}. Skipping.")
        continue

    print(f"Writing {title} to file.")
    # Write to output
    with enriched_output.open('a+', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        if not header_present:
            wr.writerow([k for k in paper_meta.keys()])
            header_present = True
        wr.writerow([value for _, value in paper_meta.items()])
