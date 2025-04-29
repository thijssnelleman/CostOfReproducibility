"""Enrich the scraped data using Scopus."""
import sys
import yaml
import pybliometrics
from pybliometrics.scopus import ScopusSearch
from pybliometrics.scopus import CitationOverview

import requests

scopus_api_key = yaml.safe_load(open("api_keys.yaml"))["scopus"]
pybliometrics.init(keys=[scopus_api_key])

# Testing example
title = "Joint Human Pose Estimation and Instance Segmentation with PosePlusSeg"
s = ScopusSearch(f'TITLE("{title}")')

if s.results is None:
    print(f"Could not find: {title}")

if len(s.results) > 1:
    print(f"Multiple results for: {title}")
    sys.exit(-1)

paper_meta = s.results[0]
paper_meta = {name: item for name, item in zip(paper_meta._fields, paper_meta)}

# It is currently not possible to acquire more data due to authorisation issues

search_url = f"https://api.elsevier.com/content/abstract/citation-count?doi={paper_meta["doi"]}&httpAccept=application/xml"
headers = {'Accept':'application/json', 'X-ELS-APIKey': scopus_api_key}
page_request = requests.get(search_url, headers=headers)

print(page_request.content)
