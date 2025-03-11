from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

#chat template
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent.'),  # system message with domain placeholder
    MessagesPlaceholder(variable_name='chat_history'), # chat history placeholder
    ('human', '{query}') # human message with topic placeholder
])

chat_history = []
#load chat history
with open('LangChain_Prompts\chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

#create prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund?'})