# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()



model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

class Person(BaseModel):
    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description='City of the person')

parser = PydanticOutputParser(pydantic_object=Person)
template = PromptTemplate(
    template = 'Generate the name  age and city of a fictional {place} person. \n {format_instruction}',
    input_variables = ['place'],
    partial_variables = {'format_instruction': parser.get_format_instructions()}
)

# prompt = template.invoke({'place':'Indian'})
# print(prompt) # Print the prompt
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)

#using chain
chain = template | model | parser
result = chain.invoke({'place':'Italy'}) # Invoke the chain with the input text
print(result) # Print the result