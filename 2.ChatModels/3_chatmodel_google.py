from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv  # for loading environment variables

# Load the environment variables
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

result = model.invoke("What is the capital of India?") # Invoke the model with the input text

print(result.content) # Print the result the ans is in content of the result so print result.content