import json
import faiss
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import sqlite_utils as sql3
import os
from dotenv import load_dotenv
import openai
import sys

#### Suggested questions ####
#question = 'When will the fried Sam Bankman trial be?'
#question = 'Does Coinbase have its own blockchain?'
#question = 'When will the Spot Bitcoin ETF be approved?'
#question = 'What happened in November 2022 with FTX?'
#question = 'Are FTX related scams happening?'

os.environ['TOKENIZERS_PARALLELISM'] = 'false'

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

db = sql3.Database("../database/database.sqlite")
dbNews = db['news']

def search(question):
    newsArray = list(dbNews.rows)
    embeddings = []

    for new in newsArray:
        embedding = np.array(json.loads(new['embedding']))
        embeddings.append(embedding)

    embeddings = np.array(embeddings, dtype=np.float32)

    vectorDimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(vectorDimension)

    faiss.normalize_L2(embeddings)
    index.add(embeddings)

    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

    query_vector = model.encode(question)
    query_vector = np.array([query_vector])
    faiss.normalize_L2(query_vector)


    k = 10
    distances, indices = index.search(query_vector, k)

    infoForGPT = []
    newsRecords = []
    for idx, distance in zip(indices[0], distances[0]):
        infoForGPT.append({'title': newsArray[idx]['title'], 'text': newsArray[idx]['text']})
        newsRecords.append({
            'name': newsArray[idx]['title'],
            'url': newsArray[idx]['news_url'],
        })
        #print(f"Title: {newsArray[idx]['title']}")
        #print(f"Similarity: {distance}")

    chatCompletion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
        {"role": "system", "content": 'You must answer in detail the question asked by the user, based on the information provided by the assistant. In the response to the user, do not mention that the information comes from news and articles, you have to respond as if you knew the answer before receiving the news that I provide (although you must use that information to generate the response), Limit yourself to giving the answer and don\'t mention where you got the information from.'},
        {"role": "assistant", "content": 'Below I am going to provide you with news information (in JSON format), which is related to the question asked by the user:' + json.dumps(infoForGPT)},
        {"role": "user", "content": question}
    ])
    responseMessage = chatCompletion.choices[0].message['content']
    return responseMessage, newsRecords


if len(sys.argv) > 1:
    question = sys.argv[1]
    completion, records = search(question)

    print(json.dumps({
        'completion': completion,
        'records': records
    }))
else:
    print('You must pass the search parameter, example: python3 search.py \"What happened in November 2022 with FTX?\"')
