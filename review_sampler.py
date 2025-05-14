"""Stratified random sampling of reviews for 2nd review."""
import argparse
import ast
import pandas as pd

def arg_parser() -> argparse.ArgumentParser:
    """Create the sampling argument parser"""
    parser = argparse.ArgumentParser(description="Sample papers from a conference/journal")
    parser.add_argument("--source", type=str, help="Choose the source to sample from (AAAI, ICML, IJCAI, JAIR, JMLR)", required=True)
    parser.add_argument("--sample-size", type=int, help="Choose the number of papers to sample PER STRATUM:", required=True)
    return parser

def sample_reviews(sample_size: int, source: str) -> None:
    """Randomdly sample n reviews from a specific year from a conference/journal."""
    review_data = pd.read_csv("reviews.csv")
    meta = []
    for y in [2022, 2023, 2024]:
        meta.append(pd.read_csv(f"{source}/{y}/Proceedings/meta.csv"))
        meta[-1]["Year"] = y
    meta = pd.concat(meta)

    # Filter
    review_data = review_data[review_data["source"] == source]
    review_data = review_data[review_data["theoretical"] == False]

    # Caclulate the average rating for each paper (Excluding expertise)
    review_data["average_rating"] = review_data[["Implementation", "Data", "Configuration", "Expertise"]].mean(axis=1)
    # Place each paper in a stratum based on the rating: bottom 33% of papers, middle 33% of papers, top 33% of papers
    review_data["stratum"] = pd.qcut(review_data["average_rating"], 3, labels=["Low", "Middle", "High"])

    sample = pd.concat([review_data[review_data["stratum"] == "Low"].sample(n=sample_size),
                        review_data[review_data["stratum"] == "Middle"].sample(n=sample_size),
                        review_data[review_data["stratum"] == "High"].sample(n=sample_size)])

    
    meta_rows = []
    for _, row in sample.iterrows():
        title = row["title"]
        rowm = meta[meta["Title"] == title]
        rowm["stratum"] = row["stratum"]
        meta_rows.append(rowm)

    meta_rows = pd.concat(meta_rows)[["Title", "Year", "Authors", "stratum", "pdf_url"]]
    for row in meta_rows.index:
        try:
            meta_rows.at[row, "Authors"] = ", ".join(ast.literal_eval(meta_rows.at[row, "Authors"]))
        except:
            pass

    print(meta_rows)
        

if __name__ == "__main__":
    pd.set_option("display.max_colwidth", None)
    pd.set_option("display.max_columns", None)  
    parser = arg_parser()
    args = parser.parse_args()
    
    # Sample stratified over the given year and source
    sample_reviews(args.sample_size, args.source)
