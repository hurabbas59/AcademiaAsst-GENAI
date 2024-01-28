import json
import re
import ast

def parse_json(json_data):
    
    try:
        # If the input is a string, parse it as a single JSON object
        if isinstance(json_data, str):
            parsed_data = json.loads(json_data,strict=True)
            return parsed_data
        # If the input is a list, parse each element as a JSON object
        elif isinstance(json_data, list):
            parsed_data = []
            for item in json_data:
                parsed_item = json.loads(item,strict=True)
                parsed_data.append(parsed_item)
    except Exception:
        parsed_data = ast.literal_eval(json_data)

    return parsed_data
    
def parse_dict(text):
    regex = r"\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}"
    matches = re.findall(regex, text, re.DOTALL)
    list = []
    for x in matches:
        list.append(json.loads(x))
    return list
