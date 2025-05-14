"""AAAI publication webscraper."""
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import csv
import sys

base = "https://ojs.aaai.org/index.php/AAAI/issue/view/"
header = {  # Spoof user agent
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
}

# Webpage numbers where the publications can be found
year_ranges = {"2024": list(range(576, 597)),
               "2023": list(range(548, 560)),
               "2022": list(range(507, 514)) + [519, 520, 521],
               "2021": list(range(385, 402))}

if len(sys.argv) == 1:
    print("Which year are you interested in?")
    year = input()
else:
    year = sys.argv[1]

if year not in year_ranges:
    print("Invalid year. Choose from: ", year_ranges.keys())
    sys.exit(-1)

target_dir = Path(f"AAAI/{year}/Proceedings")
target_dir.mkdir(exist_ok=True, parents=True)
base = "https://ojs.aaai.org/index.php/AAAI/issue/view/"

print("Retrieving meta from: ", base)

# Make sure output csv exists
meta_csv_file = target_dir / "meta.csv"
print("Saving to: ", meta_csv_file)
with meta_csv_file.open('a+', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     if len(meta_csv_file.open('r').readlines()) == 0:
        wr.writerow(["index", "Title", "Authors", "Affiliations", "keywords", "cite_key", "abstract", "pdf_url"])

existing_ids = [l[0] for l in csv.reader(meta_csv_file.open('r'))]
total_pages = len(year_ranges)
for index, issue_page in enumerate(year_ranges[year]):
    page = requests.get(base + str(issue_page), headers=header)
    soup = BeautifulSoup(page.content, "lxml")
    # Find all paper titles inside <div> tags
    for div in soup.find_all("div"):
        divclass = div.get("class")
        if divclass is not None and "obj_article_summary" in divclass:
            paper_id = paper_links[0]['id'].replace("article-", "")
            print(f"\t({index+1}/{total_pages})[{paper_id}] Title: {paper_title}")
            if paper_id in existing_ids:
                print(f"\tSkipping as it already exists")
            paper_links = div.find_all("a")
            paper_title = paper_links[0].text.strip()
            paper_url = paper_links[0]['href']
            pdf_url = paper_links[1]['href']

            # Publication specific page for more data
            paper_page = requests.get(paper_url, headers=header)
            paper_soup = BeautifulSoup(paper_page.content, "lxml")
            authors_section = paper_soup.find("section", class_="item authors")
            key_words_section = paper_soup.find("section", class_="item keywords")
            abstract_section = paper_soup.find("section", class_="item abstract")
            author_names = []
            author_affiliations = []
            for list_item in authors_section.find_all("li"):
                author_name = list_item.find("span", class_="name").text.strip()
                author_names.append(author_name)
                author_affiliations.append(list_item.find("span", class_="affiliation").text.strip())
            key_words = [kw.strip() for kw in key_words_section.find("span", class_="value").text.strip().split(",")]
            abstract_section = abstract_section.text.strip().replace("\n", " ")
            how_to_cite = paper_soup.find("div", class_="csl-entry").text
        
            # Write meta data to CSV
            with meta_csv_file.open('a+', newline='') as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                wr.writerow([paper_id, paper_title, author_names, author_affiliations, key_words, how_to_cite, abstract_section, pdf_url])
