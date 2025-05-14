"""JMLR publication scraper."""
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

meta_csv_file = target_dir / "meta.csv"
print("Saving to: ", meta_csv_file)

if not meta_csv_file.exists():
    meta_csv_file.touch()

with meta_csv_file.open('a+', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     if len(meta_csv_file.open('r').readlines()) == 0:  # Write header
        wr.writerow(["index", "Title", "Authors", "pdf_url", "project_url", "abstract"])

existing_ids = [l[0] for l in csv.reader(meta_csv_file.open('r'))]
content = soup.find("div", {"id": "content"})
total = len(content.find_all("dl"))
for i, paper in enumerate(content.find_all("dl")):
    paper_title = paper.find("dt").text.strip()
    paper_author = paper.find("i").text.strip()
    print(f"[{i}/{total}] {paper_title}")
    # Reset values
    paper_id, paper_title, paper_author, pdf_url, project_url, abstract = "", "", "", "", "", ""
    for link in paper.find_all("a"):
        if link.text.lower().strip() == "pdf":
            pdf_url = link.attrs["href"]
            paper_id = Path(pdf_url).stem.replace("-", "")
            if paper_id in existing_ids:
                print(f"Skipping {paper_id} as it already exists")
            pdf_url = f"{jmlr_base}{pdf_url}"
        if link.text.lower().strip() == "bib":
            bib_url = link.attrs["href"]
            # Download bib
            bib = requests.get(f"{jmlr_base}{bib_url}").content.decode()
            bib = bib.replace("\n", " ").replace("\t", " ").replace("\r", " ").strip()
        if link.text.lower().strip() == "abs":
            abstract = link.attrs["href"]
            # Download abs
            paper_soup = BeautifulSoup(requests.get(f"{jmlr_base}{abstract}").content, "lxml")
            abstract = paper_soup.find("p", {"class": "abstract"}).text.strip()
            abstract = abstract.replace("\n", " ").replace("\t", " ").replace("\r", " ").strip()
        if link.text.lower().strip() == "code":
            project_url = link.attrs["href"]

    with meta_csv_file.open('a+', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow([paper_id, paper_title, paper_author, pdf_url, project_url, abstract])
