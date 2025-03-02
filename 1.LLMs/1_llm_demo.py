from langchain_openai import OpenAI
from dotenv import load_dotenv  # for loading environment variables

# Load the environment variables
load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct') # Load the model from OpenAI by making instance of object

result = llm.invoke("What is the capital of India?") # Invoke the model with the input text

print(result) # Print the result 

# Output: New Delhi

