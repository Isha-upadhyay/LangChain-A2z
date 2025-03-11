from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate([  # chatbot template
    ('system', 'You are a helpful {domain} expert.'),  # system message with domain placeholder
    ('human', 'Explain in simple terms, what is {topic}') # human message with topic placeholder
])

prompt = chat_template.invoke({'domain':'AI', 'topic':'machine learning'})
print(prompt)