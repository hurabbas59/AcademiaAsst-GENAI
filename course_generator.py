from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from prompts import module_creator, module_content_outline_creator, module_outline_creator,json_prompt, theoretical_content_creator, technical_content_creator
from parsers import parse_json
class CourseGenerator:
    
    def __init__(self,model_name='gpt-3.5-turbo-16k-0613',temperature=0,streaming=False):
        
        OPENAI_API_KEY= "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"
        self.model  = ChatOpenAI(
            openai_api_key=OPENAI_API_KEY,
            model_name=model_name,
            temperature=temperature,
            request_timeout=180,
            streaming=streaming)


    def func_module_creator(self,course_title: str,semester: int):
        prompt = PromptTemplate(template = module_creator,input_variables=["course_title","semester"])
            
        chain = LLMChain(llm=self.model,prompt=prompt)
        
        response = chain.run(**{"course_title":course_title,
                                "semester":semester
                            })
        

        return response
    
    def func_module_outline_creator(self,course_name,course_code,credit_hours):
        prompt = PromptTemplate(template = module_outline_creator,input_variables=["course_name","course_code","credit_hours"])
            
        chain = LLMChain(llm=self.model,prompt=prompt)
        
        response = chain.run(**{"course_name":course_name,
                                "course_code":course_code,
                                "credit_hours":credit_hours
                            })
        

        return response

    def func_module_content_outline_creator(self,module_name,module_description,semester):
        prompt = PromptTemplate(template = module_content_outline_creator,input_variables=["module_name","module_description","semester"])
            
        chain = LLMChain(llm=self.model,prompt=prompt)
        
        response = chain.run(**{"module_name":module_name,"module_description":module_description,"semester":semester})
        
        return response
    def json_converter(self,json_text):
        prompt = PromptTemplate(template=json_prompt,input_variables=["json"])
        
        chain = LLMChain(llm=self.model,prompt=prompt)
        
        response = chain.run({"json":json_text})
        
        return response
    
    def func_theoretical_content_creator(self,sub_section,detailed_description,semester):
        prompt = PromptTemplate(template = theoretical_content_creator,input_variables=["sub_section","detailed_description","semester"])
            
        chain = LLMChain(llm=self.model,prompt=prompt)
        
        response = chain.run(**{"sub_section":sub_section,"detailed_description":detailed_description,"semester":semester})
        
        return response
    
    
    
    def func_technical_content_creator(self,sub_section,detailed_description,semester):
        prompt = PromptTemplate(template = technical_content_creator,input_variables=["sub_section","detailed_description","semester"])
            
        chain = LLMChain(llm=self.model,prompt=prompt)
        
        response = chain.run(**{"sub_section":sub_section,"detailed_description":detailed_description,"semester":semester})
        
        return response
        
        
        
   