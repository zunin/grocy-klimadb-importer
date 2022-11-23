import re
import requests
from grocy.auth import APIKeyAuth

req = requests.get(f'{os.environ['GROCY_API_URI']}/openapi/specification', auth=APIKeyAuth())
req.raise_for_status()
json = req.json()

def strip_brackets(instr: str) -> str: 
    return instr.replace('{', '').replace("}", "")

paths = json['paths']
for path in paths.keys():
    keyword_search = re.findall(r"{\w+}", path)
    keywords = [strip_brackets(keyword)for keyword in keyword_search]
    operationId = path[1:].replace("/", "_").replace("-", "_")
    if keywords:
        for keyword in keyword_search:
            operationId = operationId.replace(keyword, "by_"+strip_brackets(keyword))
        line_to_print = operationId.upper() + " = lambda " + ", ".join(keywords) + ": f\""+path+"\""
        print(line_to_print)
    else:
        print(operationId.upper() + " = \""+path+"\"")
