import json
from pathlib import Path

PROJECT_ROOT =  Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT /"data"/"movies.json"
STOPWORDS_PATH = PROJECT_ROOT /"data"/"stopwords.txt"

def load_movies():
    with open(DATA_PATH, "r") as f:
        data = json.load(f)
    return data["movies"]

def load_stopwords():
    with open(STOPWORDS_PATH, "r") as f:
        data = f.read().splitlines()
    return data