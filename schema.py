from pydantic import BaseModel
from typing import List, Dict,Any

class ModuleCreatorRequest(BaseModel):
    file: str

# class ModuleCreatorRequest(BaseModel):
#     course_title: str
#     semester: int


class ModuleResponse(BaseModel):
    response: Any
    
class ModuleOutlineCreatorRequest(BaseModel):
    semester: int

class ModuleContentCreatorRequest(ModuleOutlineCreatorRequest):
    course_outline: List[Any]
    course_type: str
    
class ExamGeneratorRequest(BaseModel):
    course_name: str
    course_type: str
    difficulty_level:str
    exam_time: str
    semester: str
    topics_to_include:str


class ModuleContentCreatorRequest(BaseModel):
    course_type: str
    course_title: str
    semester: int