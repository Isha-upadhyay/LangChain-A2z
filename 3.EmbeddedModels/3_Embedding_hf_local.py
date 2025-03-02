from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-mpnet-base-v2')

# text = "Delhi is the capital of India"

documents = [
    "Delhi is the Capital of India",
    "Kolkata is capital of West Bengal",
    "Paris is the capital of Frane"
]
vector = embedding.embed_documents(documents)
print(str(vector))