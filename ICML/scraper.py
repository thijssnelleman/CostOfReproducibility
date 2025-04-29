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

icml_base = "https://www.icml.cc/"
base = f"{icml_base}/virtual/{year}/papers.html?filter=titles"
target_dir = Path(f"ICML/{year}/Proceedings")
page = requests.get(base)
soup = BeautifulSoup(page.content, "lxml")

links = []
for link in soup.find_all("a"):
    if "href" in link.attrs and "virtual" in link.attrs["href"] and "poster" in link.attrs["href"]:
        links.append(link.attrs["href"])

print("Retrieving from: ", base)

ids = []
titles = []
authors = []
pdf_urls = []
project_urls = []
abstracts = []
#how_to_cites = []

meta_csv_file = target_dir / "meta.csv"
print("Saving to: ", meta_csv_file)

if not meta_csv_file.exists():
    meta_csv_file.touch()

with meta_csv_file.open('a+', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     if len(meta_csv_file.open('r').readlines()) == 0:
        wr.writerow(["index", "Title", "Authors", "pdf_url", "project_url", "abstract"])

existing_ids = [l[0] for l in csv.reader(meta_csv_file.open('r'))]
# Find all paper titles inside <div> tags
for link_index, l in enumerate(links):
    if "accounts/login?nextp=" in l:
        continue

    id = l.split("/")[-1]
    if id in existing_ids:
        print(f"Skipping {id} as it already exists")
        continue

    paper_soup = BeautifulSoup(requests.get(f"{icml_base}{l}").content, "lxml")
    project_url = ""
    how_to_cite = ""
    pdf_url = ""
    title = paper_soup.find("h2", class_="card-title main-title text-center").text.strip()
    author = paper_soup.find("h3", class_="card-subtitle mb-2 text-muted text-center").text.strip().split(" · ")

    for link in paper_soup.find_all("a"):
        if "href" in link.attrs and "paper pdf" in link.text.lower():
            intermediate = link.attrs["href"]
            another_soup = BeautifulSoup(requests.get(intermediate).content, "lxml")
            for mlrlinks in another_soup.find_all("a"):
                if "href" in mlrlinks.attrs and "pdf" in mlrlinks.attrs["href"] and "download pdf" in mlrlinks.text.lower():
                    pdf_url = mlrlinks.attrs["href"]
        if "href" in link.attrs and "pdf" in link.text.lower() and "btn btn btn-outline-dark btn-sm href_Poster" in " ".join(link.attrs["class"]):
            pdf_url = link.attrs["href"]
        if "href" in link.attrs and "project" in link.attrs["href"]:
            project_url = link.attrs["href"]  # Implementation links

    abstract = str(paper_soup.find("div", id="abstractExample").text).strip().strip("Abstract:").strip().replace("\n", " ")
    titles.append(title)
    abstracts.append(abstract)
    project_urls.append(project_url)
    ids.append(id)
    authors.append(author)
    pdf_urls.append(pdf_url)
    print(f"({link_index}/{len(links)}) [{id}] Title: {title}")
    # Write meta data to CSV
    with meta_csv_file.open('a+', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        if ids[-1] in existing_ids:
            print(f"Skipping {ids[-1]} as it already exists")
            continue
        wr.writerow([ids[-1], titles[-1], authors[-1], pdf_urls[-1], project_urls[-1], abstracts[-1]])

if not (len(titles) == len(authors) == len(pdf_urls)):
    print("ERROR: The lengths of Titles/Authors/PDFs vary: ",
          len(titles), len(authors), len(pdf_urls))
    sys.exit(-1)



