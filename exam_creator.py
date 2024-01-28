from prompts import theoretical_exam_prompt,technical_exam_prompt
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI


class ExamCreator:
    
    def __init__(self,model_name='gpt-3.5-turbo',temperature=0,streaming=False):
        OPENAI_API_KEY= "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"

        self.model  = ChatOpenAI(
            openai_api_key=OPENAI_API_KEY,
            model_name=model_name,
            temperature=temperature,
            request_timeout=180,
            streaming=streaming)
    
        

    def func_generate_exam(self,course_name,course_type,difficulty_level,exam_time,semester,topics_to_include):
        
        if course_type.lower()=="theoretical":
            prompt = PromptTemplate(template = theoretical_exam_prompt,input_variables=["course_name","course_type","exam_time","difficulty_level","semester","topics_to_include"])
            
            chain = LLMChain(llm=self.model,prompt=prompt)
            input_fields = {"course_name":course_name,"course_type":course_type,"exam_time":exam_time,"difficulty_level":difficulty_level,"semester":semester,"topics_to_include":topics_to_include}
            response = chain.run(**input_fields)    
            
            return response
        
        if course_type.lower()=="technical":
            prompt = PromptTemplate(template = technical_exam_prompt,input_variables=["course_name","course_type","exam_time","difficulty_level","semester","topics_to_include"])
            
            chain = LLMChain(llm=self.model,prompt=prompt)
            input_fields = {"course_name":course_name,"course_type":course_type,"exam_time":exam_time,"difficulty_level":difficulty_level,"semester":semester,"topics_to_include":topics_to_include}
            response = chain.run(**input_fields)    
            
            return response
                    
        



    