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


df_reviews = pd.read_csv(Path("reviews.csv"))

print(f"Querying {len(df_reviews)} titles...")

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

# Some little borrowing from https://stackoverflow.com/questions/33404752/removing-emojis-from-a-string-in-python
def deEmojify(text):
    import re
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)


title_map = {  # These titles have 'typos' in them on SCOPUS!
    "SVFI Spiking-Based Video Frame Interpolation for High-Speed Motion": "VFI: Spiking-Based Video Frame Interpolation for High-Speed Motion",
    "Entropy Estimation via Normalizing Flow": "Entropy Eestimation via Normalizing Flow",
    "Plurality Veto A Simple Voting Rule Achieving Optimal Metric Distortion": "PLURALITYVETO: A Simple Voting Rule Achieving Optimal Metric Distortion",
    #"Align, Perturb and Decouple Toward Better Leverage of Difference Information for RSI Change Detection": ""  # Does not exists on scopus???
    "Convergence in Multi-Issue Iterative Voting under Uncertainty": "Convergence of Multi-Issue Iterative Voting under Uncertainty",
    "MA2CLMasked Attentive Contrastive Learning for Multi-Agent Reinforcement Learning": "MA2CL:Masked Attentive Contrastive Learning for Multi-Agent Reinforcement Learning",
    "CostFormerCost Transformer for Cost Aggregation in Multi-view Stereo": "CostFormer: Cost Transformer for Cost Aggregation in Multi-view Stereo",
    "Proving the Lottery Ticket Hypothesis for Convolutional Neural Networks": "PROVING THE STRONG LOTTERY TICKET HYPOTHESIS FOR CONVOLUTIONAL NEURAL NETWORKS",
    # "Multi-Task Processes": "" # DOES NOT EXIST ON SCOPUS?
    "Symbolic Learning to Optimize Towards Interpretability and Scalability": "SYMBOLIC LEARNING TO OPTIMIZE: TOWARDS IN-TERPRETABILITY AND SCALABILITY",
    "Progressively Compressed Auto-Encoder for Self-supervised Representation Learning": "PROGRESSIVELY COMPRESSED AUTOENCODER FOR SELF-SUPERVISED REPRESENTATION LEARNING",
    "$\mathrm{SE}(3)$-Equivariant Attention Networks for Shape Reconstruction in Function Space": "SE(3)-EQUIVARIANT ATTENTION NETWORKS FOR SHAPE RECONSTRUCTION IN FUNCTION SPACE",
    "Clean-image Backdoor Attacking Multi-label Models with Poisoned Labels Only": "CLEAN-IMAGE BACKDOOR: ATTACKING MULTILABEL MODELS WITH POISONED LABELS ONLY",
    "LightHGNN Distilling Hypergraph Neural Networks into MLPs for 100x Faster Inference": "LIGHTHGNN: DISTILLING HYPERGRAPH NEURAL NETWORKS INTO MLPS FOR 100× FASTER INFERENCE",
    "pi2vec Policy Representation with Successor Features": "π2VEC: POLICY REPRESENTATION WITH SUCCESSOR FEATURES",
    "Adversarial Robustness against Multiple and Single $l_p$-Threat Models via Quick Fine-Tuning of Robust Classifiers": "Adversarial Robustness against Multiple and Single lp-Threat Models via Quick Fine-Tuning of Robust Classifiers",
    "Fast e-Approximation Algorithms for Binary Matrix Factorization": "Fast (1 + ε)-Approximation Algorithms for Binary Matrix Factorization",
    #"An empirical analysis of compute-optimal large language model training": "INFERENCE SCALING LAWS: AN EMPIRICAL ANALYSIS OF COMPUTE-OPTIMAL INFERENCE FOR LLM PROBLEM-SOLVING"
    "A High-Resolution Dataset for Instance Detection with Multi-View Object Capture": "A High-Resolution Dataset for Instance Detection with Multi-View Instance Capture",
    "MultiVENT Multilingual Videos of Events and Aligned Natural Text": "MultiVENT: Multilingual Videos of Events with Aligned Natural Text",
    "HEBO Pushing The Limits of Sample-Efficient Hyper-parameter Optimisation": "HEBO: Pushing The Limits of Sample-Efficient Hyperparameter Optimisation",
    "A Scoping Study on AI Affordances in Early Childhood Education Mapping the Global Landscape Identifying Research Gaps and  Charting Future Research Directions": "A Scoping Study of AI Affordances in Early Childhood Education: Mapping the Global Landscape, Identifying Research Gaps, and Charting Future Research Directions",
    #"Underspecification Presents Challenges for Credibility in Modern Machine Learning": "",
    "MultiZoo and MultiBench A Standardized Toolkit for Multimodal Deep Learning": "MULTIZOO & MULTIBENCH: A Standardized Toolkit for Multimodal Deep Learning",
}

for index_row, row in df_reviews.iterrows():
    title = row["title"]
    year = row["year"]
    source = row["source"]

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
        #print(search_title)
        if search_title in title_map.keys():
            #print(f"[!] Mapping search of {search_title} to {title_map[search_title]}")
            search_title = title_map[search_title]
        s = ScopusSearch(f'TITLE("{search_title}") AND PUBYEAR = {row["year"]} AND NOT TITLE("Extended Abstract")')
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
        print(f"Could not find: '{title}' (Search: '{search_title}')")
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

            print(f"\t[{index}] {option['title']} ({option['publicationName']})")
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
