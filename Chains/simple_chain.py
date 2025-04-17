from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    inout_variables=['topic']    
)

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

pareser = StrOutputParser()

chain = prompt | model | pareser 


result = chain.invoke({'topic':'Cricket'})
# print(result)

chain.get_graph().print_ascii() #visualize chain through this method
