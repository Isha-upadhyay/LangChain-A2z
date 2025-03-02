from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv  # for loading environment variables

# Load the environment variables
load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

result = embedding.embed_query("Delhi is the Capita of India")

print(str(result))



