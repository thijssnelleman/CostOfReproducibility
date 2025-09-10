"""Extracts the results of each review and compiles it into one CSV file."""
from pathlib import Path
import sys
import re
import csv

url_regex = r"\b(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]*[-A-Za-z0-9+&@#/%=~_|]"
data_count_regex = r"\((?P<public>\d+)/(?P<total>\d+)\)"

def extract_file(file_path: Path, skip_datasets: bool = False) -> dict:
    """Extract the results from a single review."""
    review = file_path.open().read()
    sections = review.split("###")    
    meta, sections = sections[0], sections[1:]
    meta = [l.strip() for l in meta.splitlines() if l.strip() != ""]
    theoretical = False
    if meta[-1].lower().startswith("[x]"):
        theoretical = True
        meta = meta[:-1]
    if meta[-1].lower().startswith("project url:"):
        meta = meta[:-1]
    paper_title = meta[0].replace("## ", "")
    authors = meta[1]
    keywords = meta[2].replace("Keywords: ", "")
    awards = ""
    if len(meta) == 5:
        awards = meta[3].replace("Award: ", "")
        pdf_path = meta[4]
    else:
        pdf_path = meta[3]

    index = Path(pdf_path).stem.split(" - ", maxsplit=1)[0]
    result = {"title": paper_title, "authors": authors, 
              "keywords": keywords, "index": index, "pdf_path": pdf_path,
              "awards": awards, "theoretical": theoretical,
              "implementation_url": None, "public_datasets": None, "total_datasets": None}
    public_datasets, total_datasets = None, None
    for s in sections:
        lines = [l.strip() for l in s.splitlines() if l.strip() != ""]
        title = lines[0]
        cost = lines[2][1:-1]
        if title == "Data" and not skip_datasets:
            if not re.match(data_count_regex, lines[3]):
                print("ERROR in review regarding data set counter:", file_path)
                sys.exit(-1)
            public_datasets, total_datasets = re.match(data_count_regex, lines[3]).groups()
        # Check the value is an int in the correct range
        try:
            cost = int(cost)
            assert cost >= 1 and cost <= 10
        except ValueError:
            print("ERROR in review:", file_path)
            sys.exit(-1)
        explanation = lines[3:]
        if title == "Implementation":
            url_search = re.search(url_regex, " ".join(explanation))
            if url_search:
               result["implementation_url"] = url_search.group(0)
            else:
                result["implementation_url"] = None
        explanation = " ".join(explanation)
        result[title] = cost
        result[f"{title}_appendix_mentions"] = explanation.lower().count("appendix")
        result[f"{title}_checklist_mentions"] = explanation.lower().count("checklist")
    result["public_datasets"] = public_datasets
    result["total_datasets"] = total_datasets
    if not skip_datasets:
        try:        
            assert result["public_datasets"] is not None
            assert result["total_datasets"] is not None
        except AssertionError:
            print("ERROR in review:", file_path)
            print(result)
            sys.exit(-1)
    return result

def main():
    """First compile the regular reviews, then the 2nd reviews."""
    target = Path("reviews.csv")

    sources = ["AAAI", "IJCAI", "ICLR", "ICML", "NeurIPS", "JAIR", "JMLR"]
    years = ["2022", "2023", "2024"]

    rows = [["source", "year"]]
    for source in sources:
        for year in years:
            for file in (Path(source) / year / "reviews").iterdir():
                if not file.suffix == ".md":
                    continue
                result = extract_file(file)
                if result is None:
                    continue
                if len(rows) == 1:
                    rows[0].extend(list(result.keys()))
                rows.append([source, year] + list(result.values()))

    with target.open("w") as f:
        csv_writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_MINIMAL)
        for r in rows:
            r = [str(e) for e in r]
            csv_writer.writerow(r)

    # Compile the second reviews
    rows = [["source", "year"]]
    target = Path("2nd_reviews.csv")
    for source in sources:
        for year in years:
            for file in (Path(source) / year / "reviews" / "2nd reviews").iterdir():
                if not file.suffix == ".md":
                    continue
                result = extract_file(file, skip_datasets=True)
                if result is None:
                    continue
                if len(rows) == 1:
                    rows[0].extend(list(result.keys()))
                rows.append([source, year] + list(result.values()))

    with target.open("w") as f:
        csv_writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_MINIMAL)
        for r in rows:
            r = [str(e) for e in r]
            csv_writer.writerow(r)

if __name__ == "__main__":
    main()