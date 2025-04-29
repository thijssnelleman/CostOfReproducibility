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

spoof_header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
}

year_map = {2022: [1162, 1163, 1164], 2023: [1165, 1166, 1167], 2024: [1168, 1169, 1170]}

jair_base = "https://www.jair.org"
target_dir = Path(f"JAIR/{year}/Proceedings")

meta_csv_file = target_dir / "meta.csv"
print("Saving to: ", meta_csv_file)

if not meta_csv_file.exists():
    meta_csv_file.touch()

with meta_csv_file.open('a+', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     if len(meta_csv_file.open('r').readlines()) == 0:
        wr.writerow(["index", "Title", "Authors", "Affiliations", "pdf_url", "abstract"])

existing_ids = [l[0] for l in csv.reader(meta_csv_file.open('r'))]

for issue_index, issue in enumerate(year_map[year]):
    base = f"{jair_base}/index.php/jair/issue/view/{issue}"
    print("Retrieving from: ", base)
    page = requests.get(base, headers=spoof_header)
    soup = BeautifulSoup(page.content, "lxml")
    total_papers_on_page = len(soup.find_all('div', {'class': 'article-summary media'}))
    for p_index, paper in enumerate(soup.find_all("div", {"class": "article-summary media"})):
        paper_url = paper.find("a").attrs["href"]
        id = paper_url.split("/")[-1]
        if id in existing_ids:
            print(f"Skipping {id} as it already exists")
            continue
        paper_soup = BeautifulSoup(requests.get(paper_url, headers=spoof_header).content, "lxml")
        abstract = paper_soup.find("div", {"class": "article-abstract"}).text.strip()
        abstract = abstract.replace("\n", " ").replace("\t", " ").replace("\r", " ").strip()
        title = paper_soup.find("h1", {"class": "page-header"}).text.strip()
        pdf_url = paper_soup.find("a", {"class": "galley-link btn btn-primary pdf"}).attrs["href"].replace("/view/", "/download/")

        # Fetch author data
        paper_authors = []
        paper_authors_affiliations = []
        for author_div in paper_soup.find_all("div", {"class": "author"}):
            paper_authors.append(author_div.find("strong").text.strip())
            # Attempt to find affiliation of the author
            affiliation_div = author_div.find("div", {"class": "article-author-affilitation"})
            if affiliation_div is not None:
                affiliation = affiliation_div.text.strip()
                if '"' in affiliation:  # Sometimes the formatting is in json style
                    affiliation = affiliation.split('"')[-2].strip()
                paper_authors_affiliations.append(affiliation)
            else:
                paper_authors_affiliations.append("")

        print(f"({issue_index + 1}/{len(year_map[year])}, {p_index + 1}/{total_papers_on_page}) [{id}] Title: {title}")
        with meta_csv_file.open('a+', newline='') as myfile:  # Write meta data to CSV
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow([id, title, ", ".join(paper_authors), ", ".join(paper_authors_affiliations), pdf_url, abstract])
