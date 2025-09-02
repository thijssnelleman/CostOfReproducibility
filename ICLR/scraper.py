"""ICLR publication scraper."""
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


iclr_base = "https://iclr.cc"
base = f"{iclr_base}/virtual/{year}/papers.html"
target_dir = Path(f"ICLR/{year}/Proceedings")

if not target_dir.exists():
    target_dir.mkdir(parents=True)

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
paper_urls = [l[3] for l in csv.reader(meta_csv_file.open('r'))]

# back off for openreview
openreview_count = 0
# Find all paper titles inside <div> tags
for link_index, l in enumerate(links):
    resolving = False
    if "accounts/login?nextp=" in l:
        continue

    paper_id = str(l.split("/")[-1])
    if paper_id in existing_ids:
        if paper_urls[existing_ids.index(paper_id)] == "":
            print("Trying to resolve missing paper URL...")
            resolving = True
        else:
            print(f"Skipping {paper_id} as it already exists")
            continue

    paper_soup = BeautifulSoup(requests.get(f"{iclr_base}{l}").content, "lxml")
    project_url = ""
    how_to_cite = ""
    pdf_url = ""
    try:
        paper_title = paper_soup.find("h2", class_="card-title main-title text-center").text.strip()
    except: # Not a paper
        continue
    author = paper_soup.find("h3", class_="card-subtitle mb-2 text-muted text-center").text.strip().split(" · ")
    for link in paper_soup.find_all("a"):
        #print(link.text.strip(), "pdf" in link.text.lower().strip())
        if "href" in link.attrs and "paper pdf" in link.text.lower():  # Extract PDF url from PMLR
            intermediate = link.attrs["href"]
            another_soup = BeautifulSoup(requests.get(intermediate).content, "lxml")
            for mlrlinks in another_soup.find_all("a"):
                if "href" in mlrlinks.attrs and "pdf" in mlrlinks.attrs["href"] and "download pdf" in mlrlinks.text.lower():
                    pdf_url = mlrlinks.attrs["href"]
        if "href" in link.attrs and "pdf" in link.text.lower().strip() and "https://proceedings.mlr.press/" in link.attrs["href"]:  # PDF url on the webpage
            publication_soup = BeautifulSoup(requests.get(link.attrs["href"]).content, "lxml")
            for mlrlinks in publication_soup.find_all("a"):
                if "href" in mlrlinks.attrs and "download pdf" in mlrlinks.text.lower():# and  in mlrlinks.attrs["href"]:
                    pdf_url = mlrlinks.attrs["href"]
                    break
        if "href" in link.attrs and "project" in link.attrs["href"]:
            project_url = link.attrs["href"]  # Implementation links
        elif "href" in link.attrs and "openreview" == link.text.lower().strip():
            # Find the implementation link and possibly paper link on openreview
            openreview_url = link.attrs["href"]
            if openreview_count >= 30:
                print("[OpenReview] Limit reached, sleeping for 15 seconds...")
                import time
                time.sleep(15)
                openreview_count = 0
            request = requests.get(openreview_url)
            openreview_count += 1
            open_soup = BeautifulSoup(request.content, "lxml")
            for openlink in open_soup.find_all("a"):
                if project_url == "" and "href" in openlink.attrs and "zip" in openlink.text.lower().strip():
                    project_url = "https://openreview.net" + openlink.attrs["href"]
                if pdf_url == "" and "href" in openlink.attrs and "title" in openlink.attrs and "pdf" in openlink.attrs["title"].lower().strip():
                    pdf_url = "https://openreview.net" + openlink.attrs["href"]
                if pdf_url != "" and project_url != "":
                    break

    abstract = str(paper_soup.find("div", id="abstractExample").text).strip().strip("Abstract:").strip().replace("\n", " ")
    print(f"({link_index}/{len(links)}) [{paper_id}] Title: {paper_title}")
    # Write meta data to CSV
    if resolving:  # Update paper URL in line
        if pdf_url == "":
            print(f"Failed to resolve PDF url for {paper_id}")
            continue
        with meta_csv_file.open('r') as f:
            reader = csv.reader(f)
            data = list(reader)
        data[existing_ids.index(paper_id)][3] = pdf_url
        with meta_csv_file.open('w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
    
    with meta_csv_file.open('a+', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        if paper_id in existing_ids:
            print(f"\t\tSkipping {paper_id} as it already exists")
            continue
        wr.writerow([paper_id, paper_title, author, pdf_url, project_url, abstract])
        existing_ids.append(paper_id)
