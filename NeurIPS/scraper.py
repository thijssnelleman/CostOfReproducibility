from pathlib import Path
import requests
from bs4 import BeautifulSoup
import csv
import sys
import warnings
from urllib3.exceptions import InsecureRequestWarning

if len(sys.argv) == 1:
    print("Which year are you interested in?")
    year = input()
else:
    year = sys.argv[1]

# Spoof user agent
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
}

neurips_base = "https://neurips.cc"
neurips_proceedings_base = "https://proceedings.neurips.cc"
base = f"{neurips_base}/virtual/{year}/papers.html?filter=titles"
target_dir = Path(f"NeurIPS/{year}/Proceedings")

# Disable HTTPS warnings
warnings.filterwarnings("ignore", category=InsecureRequestWarning)

page = requests.get(base, headers=header, verify=False)
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
        wr.writerow(["index", "Title", "Authors", "pdf_url", "abstract"])

existing_ids = [l[0] for l in csv.reader(meta_csv_file.open('r'))]
# Find all paper titles inside <div> tags
for link_index, l in enumerate(links):
    if "accounts/login?nextp=" in l or "/poster/" not in l:
        continue

    paper_id = l.split("/")[-1]
    if paper_id in existing_ids:
        print(f"Skipping {paper_id} as it already exists")
        continue
    paper_soup = BeautifulSoup(requests.get(f"{neurips_base}{l}", headers=header, verify=False).content, "lxml")
    pdf_url = ""  # Reset data
    paper_title = paper_soup.find("h2", class_="card-title main-title text-center").text.strip()
    paper_author = paper_soup.find("h3", class_="card-subtitle mb-2 text-muted text-center").text.strip().split(" · ")
    for link in paper_soup.find_all("a"):
        if "href" in link.attrs and link.text.lower().strip() == "paper":
            intermediate = link.attrs["href"]
            another_soup = BeautifulSoup(requests.get(intermediate, headers=header, verify=False).content, "lxml")
            for paper_page_links in another_soup.find_all("a"):
                if "href" in paper_page_links.attrs and "pdf" in paper_page_links.attrs["href"] and paper_page_links.text.lower().strip() == "paper":
                    pdf_url = neurips_proceedings_base + paper_page_links.attrs["href"]
        if "href" in link.attrs and "pdf" in link.text.lower() and "btn btn btn-outline-dark btn-sm href_Poster" in " ".join(link.attrs["class"]):
            pdf_url = link.attrs["href"]

    abstract = str(paper_soup.find("div", id="abstractExample").text).strip().strip("Abstract:").strip().replace("\n", " ")
    print(f"({link_index}/{len(links)}) [{paper_id}] Title: {paper_title}")
    # Write meta data to CSV
    with meta_csv_file.open('a+', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow([paper_id, paper_title, paper_author, pdf_url, abstract])
