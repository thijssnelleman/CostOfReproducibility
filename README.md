# Cost of Reproduciblity paper

In this repository we present the data, code and analysis used for our paper.

### Requirements

The code was run under Python 3.12.2 and the required libraries can be found and installed through the `requirements.txt` file.


### Directory structure

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

### How to run

In principle, no code has to be run as everything has already been compiled. However, if you for some reason wish to re-compile data you can run the `result_compiler.py` script which searches each `$review$.md` file from all sources and writes it to `reviews.csv` and `2nd_reviews.csv` respectively (where the second file is used for interrater agreement calculation).

Each source has a `scraper.py` file that can be run to collect all meta data of papers for a specific year. It has only been tested for 2022, 2023 and 2024 and results are placed in `meta.csv` of the Proceedings directory. Note that some have been curated/fixed manually so recompiling this may not be the best option. Note that it also may take some time as they are webscrapers and produce a lot of calls to get each webpage.

## AAAI

## ICML

## IJCAI

## NeurIPS

## JAIR

## JMLR

## How to cite