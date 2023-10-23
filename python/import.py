import json
import faiss
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import sqlite_utils as sql3
import datetime
import requests

db = sql3.Database("../database/database.sqlite")


model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

'''
dbNews = db['news']
dbNews.create({
    "id": int,
    "headline": str,
    "text": str,
    "embedding": str,
    "url": str,
    "date": datetime.date,
}, pk="id", if_not_exists=True)

# Demo...
#with open("../samples/sample-digest.json", "r") as f:
#    news = json.load(f)

for new in news['data']:
    new['embedding'] = json.dumps(model.encode(new['headline'] + ' ' + new['text']).tolist())
    dbNews.insert(new)
'''

cryptonewsAPIKey = 'yqwad7kynhnjdol63m4lkr19joibqyoidsxt6fva'
cryptonewsAPIBaseURI = "https://cryptonews-api.com/api/v1/category?section=general&items=3&page={}&token=" + cryptonewsAPIKey
nPages = 80

dbNews = db['news']
dbNews.create({
    "id": int,
    "news_url": str,
    "image_url": str,
    "title": str,
    "text": str,
    "source_name": str,
    "date": datetime.date,
    "embedding": str,
}, pk="id", if_not_exists=True)

allowedFieldsNewsTable = set(["news_url", "image_url", "title", "text", "source_name", "date", "embedding"])

for page in range(1, nPages + 1):
    response = requests.get(cryptonewsAPIBaseURI.format(page))
    if response.status_code == 200:
        newsData = response.json().get('data', [])
        for newDataSingle in newsData:
            newDataSingle = {key: value for key, value in newDataSingle.items() if key in allowedFieldsNewsTable}
            newDataSingle['embedding'] = json.dumps(model.encode(newDataSingle['title'] + ' ' + newDataSingle['text']).tolist())
            dbNews.insert(newDataSingle)

print("Finished fetching news...")
