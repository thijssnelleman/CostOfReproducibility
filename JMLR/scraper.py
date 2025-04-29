from pathlib import Path
import requests
from bs4 import BeautifulSoup
import csv
import sys

if len(sys.argv) == 1:
    print("Which year are you interested in?")
    year = input()
else:
    year = int(sys.argv[1])

year_map = {2022: "v23", 2023: "v24", 2024: "v25"}

jmlr_base = "https://jmlr.org/"
base = f"{jmlr_base}/papers/{year_map[year]}/"
target_dir = Path(f"JMLR/{year}/Proceedings")
page = requests.get(base)
soup = BeautifulSoup(page.content, "lxml")

print("Retrieving from: ", base)

ids = []
titles = []
authors = []
pdf_urls = []
project_urls = []
abstracts = []
how_to_cites = []

meta_csv_file = target_dir / "meta.csv"
print("Saving to: ", meta_csv_file)

if not meta_csv_file.exists():
    meta_csv_file.touch()

with meta_csv_file.open('a+', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     if len(meta_csv_file.open('r').readlines()) == 0:
        wr.writerow(["index", "Title", "Authors", "pdf_url", "project_url", "abstract"])

existing_ids = [l[0] for l in csv.reader(meta_csv_file.open('r'))]

content = soup.find("div", {"id": "content"})

total = len(content.find_all("dl"))

for i, paper in enumerate(content.find_all("dl")):
    title = paper.find("dt").text.strip()
    author = paper.find("i").text.strip()
    titles.append(title)
    authors.append(author)
    print(f"[{i}/{total}] {title}")
    project_url = ""
    for link in paper.find_all("a"):
        if link.text.lower().strip() == "pdf":
            pdf_url = link.attrs["href"]
            id = Path(pdf_url).stem.replace("-", "")
            ids.append(id)
            pdf_urls.append(f"{jmlr_base}{pdf_url}")
        if link.text.lower().strip() == "bib":
            bib_url = link.attrs["href"]
            # Download bib
            bib = requests.get(f"{jmlr_base}{bib_url}").content.decode()
            bib = bib.replace("\n", " ").replace("\t", " ").replace("\r", " ").strip()
            how_to_cites.append(bib)
        if link.text.lower().strip() == "abs":
            abstract = link.attrs["href"]
            # Download abs
            paper_soup = BeautifulSoup(requests.get(f"{jmlr_base}{abstract}").content, "lxml")
            abstract = paper_soup.find("p", {"class": "abstract"}).text.strip()
            abstract = abstract.replace("\n", " ").replace("\t", " ").replace("\r", " ").strip()
            abstracts.append(abstract)
        if link.text.lower().strip() == "code":
            project_url = link.attrs["href"]

    # Don't write faulty lines
    assert len(pdf_urls) == len(how_to_cites) == len(abstracts) == len(titles) == len(authors) == len(ids)

    with meta_csv_file.open('a+', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        if ids[-1] in existing_ids:
            print(f"Skipping {ids[-1]} as it already exists")
            continue
        wr.writerow([ids[-1], titles[-1], authors[-1], pdf_urls[-1], project_url, abstracts[-1]])
