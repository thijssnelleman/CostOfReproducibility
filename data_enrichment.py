"""Enrich the scraped data using Scopus."""
import yaml

scopus_api_key = yaml.safe_load(open("api_keys.yaml"))["scopus"]

