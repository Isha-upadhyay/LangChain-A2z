from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None # Optional field with default value None
    email:EmailStr
    cgpa:float = Field(gt=0, le=10, default=5 ,description="A decimal value represnting")

new_student = {'name':'isha', 'age': 22, 'email':'abc@gmail.com', 'cgpa':9.5}
student = Student(**new_student)

student_dict = dict(student)
print(student_dict['age'])

student_json = student.model_dump_json()
print(student_json)