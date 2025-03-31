from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model =   ChatOpenAI()
#schema
class Review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief smmary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review either negative, postive or neutral"]
    pros: Annotated[Optional[list[str]], "List all the pros of the product", "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "List all the cons of the product", "Write down all the pros inside a list"]

structured_model = model.with_structured_output(Review)
result = structured_model.invoke(""" Samsung Galaxy S24 Ultra Review: A Powerhouse with AI Enhancements
Key Themes:
AI Integration: Samsung’s new AI-driven features enhance productivity and camera performance.
Performance & Hardware: The Snapdragon 8 Gen 3 chip delivers top-tier speed and efficiency.
Display & Design: Stunning 6.8-inch AMOLED panel with a more durable titanium frame.
Camera Capabilities: Advanced 200MP sensor and AI-powered enhancements for superior photography.
Battery Life: Long-lasting battery with improved efficiency.
                                 
prs:
Stunning display with high brightness
Powerful performance with AI features
Versatile camera system with improved zoom
Long software support
S-Pen integration for productivity
                                 
cons:
Heavy and bulky design
Expensive pricing
Fast charging could be better
Minor design changes from previous model""")

print(result) # Print the result
