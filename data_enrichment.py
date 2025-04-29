"""Enrich the scraped data using Scopus."""
import sys
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
        already_done_titles = pd.read_csv(enriched_output)["title"].to_list()

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

for title in titles:
    # Testing example
    #title = "Joint Human Pose Estimation and Instance Segmentation with PosePlusSeg"
    if title in already_done_titles:
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
        print("Continuing...")
        input()
        continue

    if s.results is None:
        print(f"Could not find: {title}")
        if not unfindable_output.exists():
            unfindable_output.touch()
        with unfindable_output.open("a+") as fout:
            fout.write(f"{title}\n")
        continue

    if len(s.results) > 1:
        print(f"Multiple results for: {title}")
        option_list = [{name: item for name, item in zip(option._fields, option)}
                       for option in s.results]
        for index, option in enumerate(option_list):
            print(f"\t[{index}] {option['title']}")
        print("Select the index which matches best, or s to skip: ", end="")
        selection = input()
        if selection == "s":
            print("Skipping..")
            continue
        selection = int(selection)
        paper_meta = option_list[selection]
    else:
        paper_meta = s.results[0]
        paper_meta = {name: item for name, item in zip(paper_meta._fields, paper_meta)}

    if paper_meta["title"] in already_done_titles:
        print(f"Already wrote: {paper_meta["title"]}. Skipping.")

    print(f"Writing {title} to file.")
    # Write to output
    with enriched_output.open('a+', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        if not header_present:
            wr.writerow([k for k in paper_meta.keys()])
            header_present = True
        wr.writerow([value for _, value in paper_meta.items()])
