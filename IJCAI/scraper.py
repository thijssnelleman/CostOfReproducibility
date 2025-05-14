"""IJCAI website publication scraper."""
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

ijcai_base = "https://www.ijcai.org"
base = f"{ijcai_base}/proceedings/{year}/"
target_dir = Path(f"IJCAI/{year}/Proceedings")
page = requests.get(base)
soup = BeautifulSoup(page.content, "lxml")

print("Retrieving from: ", base)

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
    if divclass is not None and "paper_wrapper" in divclass:  # Found a publication
        # Get the data from the paper
        for subdiv in div.find_all("div"):
            subdivclass = subdiv.get("class")
            if subdivclass is None:
                continue
            if "title" in subdivclass:
                paper_title = subdiv.text
            elif "authors" in subdivclass:
                author = subdiv.text
            elif "details" in subdivclass:
                paper_link, details_link = subdiv.find_all("a")
                pdf_url = base + paper_link.attrs['href']
                paper_id = paper_link.attrs['href'].strip(".pdf")
                details_link = ijcai_base + details_link.attrs['href']
                paper_page = requests.get(details_link)
                paper_soup = BeautifulSoup(paper_page.content, "lxml")
                _, bibtex_link = paper_soup.find_all("a", class_="button btn-lg btn-download")
                how_to_cite = requests.get(ijcai_base + bibtex_link.attrs["href"]).content.decode()
                how_to_cite = how_to_cite.replace("\n", " ").strip()
                paper_keys = paper_soup.find("div", class_="keywords")
                key_words = []
                for list_item in paper_keys.find_all("div", class_="topic"):
                    key_words.append(list_item.text.strip())
                abstract = paper_soup.find("div", class_="col-md-12").text
                abstract = abstract.replace("\n", "").replace("\t", "").replace("\r", "").strip()

        # Write meta data to CSV
        with meta_csv_file.open('a+', newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            if paper_id in existing_ids:
                print(f"Skipping {paper_id} as it already exists")
                continue
            print(f"Writing {paper_id} to file")
            # IJCAI does not give author affiliations on website, thus one ""
            wr.writerow([paper_id, paper_title, author, "", key_words, how_to_cite, abstract, pdf_url])

