from fastapi import FastAPI
from services import generate_module, generate_module_outline, generat_exam, generate_module_content, generate_course_module
from schema import ModuleCreatorRequest, ModuleResponse, ExamGeneratorRequest, ModuleContentCreatorRequest
import uvicorn


router = FastAPI()


@router.post("/generate_course_modules",response_model=ModuleResponse)
async def get_modules(input: ModuleCreatorRequest):
   
    response = await generate_course_module(file_name = input.file)
    
    return ModuleResponse(response=response)

@router.post("/generate_exam",response_model=ModuleResponse)
async def get_exam(input: ExamGeneratorRequest):
    response = await generat_exam(course_name=input.course_name,
                                  course_type=input.course_type,
                                  difficulty_level=input.difficulty_level,
                                  exam_time=input.exam_time,
                                  semester=input.semester,
                                  topics_to_include=input.topics_to_include)
    
    return ModuleResponse(response=response)

@router.post("/generate_content",response_model=ModuleResponse)
async def get_content(input: ModuleContentCreatorRequest):

    # Create Modules
    modules_info = await generate_module(course_title=input.course_title,semester=input.semester)
    print(modules_info)

    modules_outline = await generate_module_outline(modules_info=modules_info,semester=input.semester)
    
    print(modules_outline)
    response = await generate_module_content(course_outline=modules_outline,
                                             modules_info=modules_info,
                                             course_title = input.course_title,
                                             semester=input.semester,
                                             course_type=input.course_type)
    
    return ModuleResponse(response=response)
    

if __name__ == "__main__":
    uvicorn.run(router, host="0.0.0.0", port=7000)