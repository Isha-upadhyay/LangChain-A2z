from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage # For message handling
from dotenv import load_dotenv

load_dotenv()

# Initialize the chatbot with Gemini-2.0-flash model (faster and lightweight version)
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

# Chat history to maintain conversation context
chat_history = [
    SystemMessage(content='You are a helpful assistant.'), 
] # Initial message to start the conversation

while True: 
    user_input = input('You:')  
    chat_history.append(HumanMessage(content=user_input)) # Append the user input to the chat history
    if user_input == 'exit':
        break
    result = model.invoke(chat_history) # Invoke the model with the chat history
    chat_history.append(AIMessage(content=result.content)) # Append the model response to the chat history
    print('Bot:', result.content)

print(chat_history) # Print the chat history
    