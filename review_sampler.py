"""Stratified random sampling of reviews for 2nd review."""
import argparse
import ast
import pandas as pd

def arg_parser() -> argparse.ArgumentParser:
    """Create the review sampling argument parser"""
    parser = argparse.ArgumentParser(description="Sample papers from a conference/journal")
    parser.add_argument("--source", type=str, help="Choose the source to sample from (AAAI, IJCAI, ICML, NeurIPS, JAIR, JMLR)", required=True)
    parser.add_argument("--sample-size", type=int, help="Choose the number of papers to sample PER STRATUM:", required=True)
    return parser

def sample_reviews(sample_size: int, source: str) -> None:
    """Randomdly sample n reviews from a specific year from a venue."""
    review_data = pd.read_csv("reviews.csv")
    meta = []
    for y in [2022, 2023, 2024]:
        meta.append(pd.read_csv(f"{source}/{y}/Proceedings/meta.csv"))
        meta[-1]["Year"] = y
    meta = pd.concat(meta)

    # Filter the reviews based on the venue
    review_data = review_data[review_data["source"] == source]

    # Caclulate the average rating for each paper
    review_data["average_rating"] = review_data[["Implementation", "Data", "Configuration", "Experimental Procedure", "Expertise"]].mean(axis=1)
    # Place each paper in a stratum based on the rating: bottom 33% of papers, middle 33% of papers, top 33% of papers
    review_data["stratum"] = pd.qcut(review_data["average_rating"], 3, labels=["Low", "Middle", "High"])

    # Take the sample from each review stratum
    sample = pd.concat([review_data[review_data["stratum"] == "Low"].sample(n=sample_size),
                        review_data[review_data["stratum"] == "Middle"].sample(n=sample_size),
                        review_data[review_data["stratum"] == "High"].sample(n=sample_size)])
    
    # Now we need to connect it to the original meta data scraped from the venue website
    meta_rows = []
    for _, row in sample.iterrows():
        title = row["title"]
        rowm = meta[meta["Title"] == title].copy()  # We match on the title, copy to avoid warnings (we actually want a copy)
        rowm["stratum"] = row["stratum"]  # Add the stratum to this meta data
        meta_rows.append(rowm)

    # Clean the data to show the relevant information
    meta_rows = pd.concat(meta_rows)[["Title", "Year", "Authors", "stratum", "pdf_url"]]
    for row in meta_rows.index:
        try:
            meta_rows.at[row, "Authors"] = ", ".join(ast.literal_eval(meta_rows.at[row, "Authors"]))
        except:
            pass

    print(meta_rows)
        

if __name__ == "__main__":
    # Update pandas display functionality, as we want to display biiiiiig table
    pd.set_option("display.max_colwidth", None)
    pd.set_option("display.max_columns", None)  
    parser = arg_parser()
    args = parser.parse_args()
    
    # Sample stratified over the given year and source
    sample_reviews(args.sample_size, args.source)
