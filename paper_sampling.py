import sys
import ast
import pandas as pd
from pathlib import Path
import random
import argparse
import re
import requests


def arg_parser() -> argparse.ArgumentParser:
    """Create the sampling argument parser"""
    parser = argparse.ArgumentParser(description="Sample papers from a conference/journal")
    parser.add_argument("--source", type=str, help="Choose the source to sample from (AAAI, ICML, IJCAI, JAIR, JMLR)", required=False)
    parser.add_argument("--year", type=str, help="Choose the year to sample from:", required=False)
    parser.add_argument("--sample-size", type=int, help="Choose the number of papers to sample:", required=False)
    parser.add_argument("--specific", type=Path, help="Choose a specific paper to write a review about.", required=False)
    return parser

def sample_papers(sample_size: int, source: str, year: str) -> None:
    """Randomdly sample n papers from a specific year from a conference/journal."""
    directory = Path(source) / year
    files_directory = directory / "Proceedings"
    reviews_directory = directory / "reviews"
    meta_csv = files_directory / "meta.csv"
    meta_data = pd.read_csv(meta_csv, index_col=0, dtype={0: str})

    selection = random.sample(range(0, len(meta_data.index)), sample_size)

    for s in selection:
        pdf_downloader(meta_data.columns.to_list(), meta_data.iloc[s].to_list(),
                       index=meta_data.index[s], target_dir=files_directory)
    write_review_template(meta_data, selection, reviews_directory, files_directory)

def pdf_downloader(header: list, row: list, index: str | int, target_dir: Path):
    title = row[header.index("Title")]
    title = re.sub("[$@/]","", title)
    file_name = f"{index} - {title}.pdf"
    url = row[header.index("pdf_url")]
    spoof_header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    }
    # Now that we have the link, fetch the file.
    if not Path(target_dir / file_name).exists():
        print(f"\tDownloading from: {url}")
        try:
            p1 = requests.get(url, headers=spoof_header)
            with (target_dir / file_name).open('wb') as f:
                f.write(p1.content)
        except Exception as ex:
            print("\tDownload failed: ", ex)
    else:
        print(f"\tFile already exists: {file_name}")


def write_review_template(meta_data: pd.DataFrame, selection_index: list[int], target_dir: Path, source_dir: Path) -> None:
    """Write a review template for each paper in the selection."""
    review_template = Path("review_template.md").open().read()
    for i in selection_index:
        title = meta_data.iloc[i]["Title"]
        review_file = (target_dir / (title + ".md"))
        if review_file.exists():  # Don't write the same paper twice
            continue
        review = review_template.replace("$PAPER TITLE$", meta_data.iloc[i]["Title"])
        authors = meta_data.iloc[i]["Authors"]
        project_url = ""
        if "project_url" in meta_data.columns:
            project_url = meta_data.iloc[i]["project_url"]
        if "keywords" in meta_data.columns:
            keywords = meta_data.iloc[i]["keywords"]
        else:
            keywords = ""
        try:
            authors = ", ".join(ast.literal_eval(authors))
        except:
            pass
        try:
            keywords = ", ".join(ast.literal_eval(meta_data.iloc[i]["keywords"]))
        except:
            pass
        review = review.replace("$AUTHORS$", authors)
        review = review.replace("$KEYWORDS$", keywords)
        review = review.replace("$PROJECT URL$\n", f"Project URL: {project_url}\n")
        try:
            paper_path = [p for p in source_dir.iterdir() if title in p.name][0]
        except:
            print("ERROR Can not find: ", title)
            paper_path = ""
        review = review.replace("$PAPER PATH$", str(paper_path))
        with review_file.open('w') as f:
            f.write(review)


if __name__ == "__main__":
    parser = arg_parser()
    args = parser.parse_args()
    if args.specific:
        specific = args.specific
        title = specific.stem.split(" - ", maxsplit=1)[1]
        target_dir = specific.parent.parent / "reviews"
        meta_data = pd.read_csv(specific.parent / "meta.csv", index_col=0)
        index = meta_data.index.get_loc(meta_data.index[meta_data["Title"] == title].to_list()[0])
        if not specific.exists():
            pdf_downloader(meta_data.columns.to_list(), meta_data.iloc[index].to_list(), index, specific.parent)
        write_review_template(meta_data, [index], target_dir, specific.parent)
        # retrieve the specific paper and write this one
        sys.exit()
    source = args.source
    if not source:
        print("Choose the source to sample from (AAAI, ICML, IJCAI, JAIR, JMLR):")
        source = input()
    year = args.year
    if not year:
        print("Choose the year to sample from:")
        year = input()
    sample_size = args.sample_size
    if not args.sample_size:
        print("Choose the number of papers to sample:")
        sample_size = input()

    sample_papers(sample_size, source, year)
