from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  # for loading environment variables

# Load the environment variables
load_dotenv()

model = ChatOpenAI = ChatOpenAI(model='gpt-4', temperature=1, max_completion_tokens=10) # Load the model from OpenAI by making instance of object with model name and other parameters like temperature and max_completion_tokens it limit the word

result = model.invoke("What is the capital of India?") # Invoke the model with the input text

print(result.content) # Print the result the ans is in content of the result so print result.content

# Result is not same as LLM as it is chat model and not language model 