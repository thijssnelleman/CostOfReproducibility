import os
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import csv
import sys
import re

if len(sys.argv) == 1:
    print("Which year are you interested in?")
    year = input()
else:
    year = sys.argv[1]

ijcai_base = "https://www.ijcai.org"
base = f"{ijcai_base}/proceedings/{year}/"
target_dir = Path(f"IJCAI/{year}/Proceedings")
page = requests.get(base)
soup = BeautifulSoup(page.content, "lxml")

print("Retrieving from: ", base)

ids = []
titles = []
authors = []
pdf_urls = []
authors = []
key_words = []
author_affiliations = []
abstracts = []
how_to_cites = []

meta_csv_file = target_dir / "meta.csv"
print("Saving to: ", meta_csv_file)
with meta_csv_file.open('a+', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     if len(meta_csv_file.open('r').readlines()) == 0:
        wr.writerow(["index", "Title", "Authors", "Affiliations", "keywords", "cite_key", "abstract", "pdf_url"])

existing_ids = [l[0] for l in csv.reader(meta_csv_file.open('r'))]
# Find all paper titles inside <div> tags
for div in soup.find_all("div"):
    divclass = div.get("class")
    if divclass is not None and "paper_wrapper" in divclass:
        # Get the data from the paper
        for subdiv in div.find_all("div"):
            subdivclass = subdiv.get("class")
            if subdivclass is None:
                continue
            if "title" in subdivclass:
                titles.append(subdiv.text)
            elif "authors" in subdivclass:
                authors.append(subdiv.text)
            elif "details" in subdivclass:
                paper_link, details_link = subdiv.find_all("a")
                pdf_urls.append(base + paper_link.attrs['href'])
                id = paper_link.attrs['href'].strip(".pdf")
                ids.append(id)
                details_link = ijcai_base + details_link.attrs['href']
                paper_page = requests.get(details_link)#, headers=header)
                paper_soup = BeautifulSoup(paper_page.content, "lxml")
                _, bibtex_link = paper_soup.find_all("a", class_="button btn-lg btn-download")
                cite = requests.get(ijcai_base + bibtex_link.attrs["href"]).content.decode()
                how_to_cites.append(cite.replace("\n", " ").strip())
                paper_keys = paper_soup.find("div", class_="keywords")
                keys = []
                for list_item in paper_keys.find_all("div", class_="topic"):
                    keys.append(list_item.text.strip())
                key_words.append(keys)
                abstract = paper_soup.find("div", class_="col-md-12").text
                abstract = abstract.replace("\n", "").replace("\t", "").replace("\r", "").strip()
                abstracts.append(abstract)
                # IJCAI does not give author affiliations on website.
                author_affiliations.append("")
        # Write meta data to CSV
        with meta_csv_file.open('a+', newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            if len(meta_csv_file.open('r').readlines()) == 0:
                wr.writerow(["index", "Title", "Authors", "Affiliations", "keywords", "cite_key", "abstract", "pdf_url"])
            if ids[-1] in existing_ids:
                print(f"Skipping {ids[-1]} as it already exists")
                continue
            print(f"Writing {ids[-1]} to file")
            wr.writerow([ids[-1], titles[-1], authors[-1], author_affiliations[-1], key_words[-1], how_to_cites[-1], abstracts[-1], pdf_urls[-1]])

if not (len(titles) == len(authors) == len(pdf_urls)):
    print("ERROR: The lengths of Titles/Authors/PDFs vary: ",
          len(titles), len(authors), len(pdf_urls))
    sys.exit(-1)



