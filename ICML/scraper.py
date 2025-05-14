"""ICML publication scraper."""
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import csv
import sys

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

    paper_id = l.split("/")[-1]
    if paper_id in existing_ids:
        print(f"Skipping {paper_id} as it already exists")
        continue

    paper_soup = BeautifulSoup(requests.get(f"{icml_base}{l}").content, "lxml")
    project_url = ""
    how_to_cite = ""
    pdf_url = ""
    paper_title = paper_soup.find("h2", class_="card-title main-title text-center").text.strip()
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
    print(f"({link_index}/{len(links)}) [{paper_id}] Title: {paper_title}")
    # Write meta data to CSV
    with meta_csv_file.open('a+', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        if paper_id in existing_ids:
            print(f"Skipping {paper_id} as it already exists")
            continue
        wr.writerow([paper_id, paper_title, author, pdf_url, project_url, abstract])
