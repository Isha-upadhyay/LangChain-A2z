from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-3-7-sonnet-20250219')

result = model.invoke("What is the capital of India?") # Invoke the model with the input text

print(result.content) # Print the result the ans is in content of the result so print result.content


