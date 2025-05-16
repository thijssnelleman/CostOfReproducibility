# Cost of Reproduciblity paper

In this repository we present the data, code and analysis used for our paper. If you wish to use the dataset, the most important file is reviews.csv, where all review data is compiled. The metadata of each paper is stored per venue directory.

## File index

For clarity we index each file here.

Regular files:
- 2nd_assessment_log.md  # A log of all questions asked regarding the guidelines during the second review
- 2nd_reviews.csv  # The compiled second reviews data
- Assessment guideline.pdf  # The assessment guidelines used for the reviews
- enriched_data.csv  # The enriched scopus data, procedurally created but manually curated
- guidelines questionnaire.pdf  # A questionnaire answered by each participant after 2nd reviews
- README.md  # This file
- requirements.txt  # Installation requirements for running the code in this repository
- review_template.md  # The template used for each review
- reviews.csv  # The compiled reviews used as data for the analysis
- unfindable.txt  # Temporary data file used for enriching SCOPUS data

Code:
- 2nd_review_analysis.ipynb  # This notebook contains all code used for analysing the 2nd reviews
- analysis.ipynb  # This notebook contains all general data analysis, such as paper awards etc.
- data_enrichtment.py  # This code as used for the small SCOPUS experiment in the appendix
- enriched_analysis.ipynb  # This code was used to analyse the SCOPUS enriched data in the appendix
- latex.py  # Used to generate the tables for the paper from the notebooks. The results were usually slightly modified by hand afterwards
- paper_sampling.py  # Used to randomly select papers from a venue / year, which then downloads the paper and writes a review template to be filled in
- result_compiler.py  # Compiles (And verifies!) all reviews into a single file for analysis
- review_sampler.py  # Stratified random sampling of reviews for a second review

Each source also has its own data scraper, which is explained in the structure below.

## Data Directory structure

Each source used for this project is placed in its own directory in accordance to the following structure:

```bash
|-- $SOURCE_NAME$
|   |-- scraper.py
|   |-- $YEAR$
|      |-- Proceedings
|           |-- $ID - $PAPER_NAME$.pdf
|           |-- meta.csv    # I contain the meta data on all papers from this year
|      |-- reviews
|           |-- $PAPER_NAME$.md  # I contain the review of the paper
|           |-- 2nd reviews
|               |-- $PAPER_NAME$.md  # I contain the second review of a paper already reviewed
```

## Running Code

### Requirements

The code was run under Python 3.12.2 and the required libraries can be found and installed through the `requirements.txt` file.

### How to run

In principle, no code has to be run as everything has already been compiled. However, if you for some reason wish to re-compile data you can run the `result_compiler.py` script which searches each `$review$.md` file from all sources and writes it to `reviews.csv` and `2nd_reviews.csv` respectively (where the second file is used for interrater agreement calculation).

Each source has a `scraper.py` file that can be run to collect all meta data of papers for a specific year. It has only been tested for 2022, 2023 and 2024 and results are placed in `meta.csv` of the Proceedings directory. Note that some have been curated/fixed manually so recompiling this may not be the best option. Note that it also may take some time as they are webscrapers and produce a lot of calls to get each webpage.

## Data License

Our dataset is free to use and adapt under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license ([CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)). To credit, see the citation instructions below.

## How to cite
