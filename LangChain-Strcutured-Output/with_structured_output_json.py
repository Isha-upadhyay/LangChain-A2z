from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model =   ChatOpenAI()

#schema
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg", "neutral"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros inside a list",
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the review",
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}

structured_model = model.with_structured_output(json_schema)
result = structured_model.invoke(""" Samsung Galaxy S24 Ultra Review: A Powerhouse with AI Enhancements
Samsung Galaxy S24 Ultra Review: A Powerhouse with AI Enhancements

Key Themes:
AI Integration: Samsung’s new AI-driven features enhance productivity and camera performance.
Performance & Hardware: The Snapdragon 8 Gen 3 chip delivers top-tier speed and efficiency.
Display & Design: Stunning 6.8-inch AMOLED panel with a more durable titanium frame.
Camera Capabilities: Advanced 200MP sensor and AI-powered enhancements for superior photography.
Battery Life: Long-lasting battery with improved efficiency.

Pros:
- Stunning display with high brightness
- Powerful performance with AI features
- Versatile camera system with improved zoom
- Long software support
- S-Pen integration for productivity.

Cons (Make sure to include this field):
- Heavy and bulky design
- Expensive pricing
- Fast charging could be better
- Minor design changes from the previous model.

Reviewer Name (Ensure this field is captured): Isha Upadhyay""")

print(result) # Print the result
