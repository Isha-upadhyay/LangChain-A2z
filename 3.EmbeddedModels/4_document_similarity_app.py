from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimension=300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership skills. He has captained India across all formats and has numerous records in international cricket.",
    "Sachin Tendulkar, also known as the 'God of Cricket,' is regarded as one of the greatest batsmen of all time. He was the first player to score 100 international centuries.",
    "MS Dhoni is a former Indian captain and wicketkeeper-batsman known for his calm demeanor and exceptional finishing abilities. Under his leadership, India won the 2007 T20 World Cup and the 2011 ODI World Cup.",
    "AB de Villiers, a South African cricketer, was famous for his 360-degree shot-making ability. He played key roles for South Africa and in various T20 leagues worldwide.",
    "Ben Stokes is an English all-rounder known for his match-winning performances, including his heroic innings in the 2019 ICC Cricket World Cup final.",
]

query = 'tell me about virat kohli'

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0] #similarity is in 2D always

index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("Similarity score is:", score)



