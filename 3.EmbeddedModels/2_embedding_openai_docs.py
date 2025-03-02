from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv  # for loading environment variables

# Load the environment variables
load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "Delhi is the Capital of India",
    "Kolkata is capital of West Bengal",
    "Paris is the capital of Frane"
]
result = embedding.embed_query(documents)
print(str(result))

