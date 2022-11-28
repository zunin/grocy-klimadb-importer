import re
import os
import requests
from typing import List, Generator, Callable, Union
from collections import namedtuple
from grocy.auth import APIKeyAuth

req = requests.get(f"{os.environ.get('GROCY_API_URI')}/openapi/specification", auth=APIKeyAuth())
req.raise_for_status()
json = req.json()

def strip_brackets(instr: str) -> str: 
    return instr.replace('{', '').replace("}", "")

def get_configuration_id(path: str) -> str:
    return path[1:].replace("/", "_").replace("-", "_")

def get_keywords(path: str) -> List[str]:
    return re.findall(r"{\w+}", path)

def create_line_from_path_and_keywords(path: str, operationId: str, keywords: List[str]) -> Callable:
    stripped_keywords = [strip_brackets(keyword)for keyword in keywords]
    for keyword in keywords:
        operationId = operationId.replace(keyword, "by_"+strip_brackets(keyword))
    return f'lambda {", ".join(stripped_keywords)}: f"{path}"'


def create_line_from_path(path: str) -> str:
    return f'"{path}"'


def _create_line(path: str, operationId: str, keywords: List[str]) -> Union[str, Callable]:
    if keywords:
        return (create_line_from_path_and_keywords(path, operationId, keywords))
    else:
        return (create_line_from_path(path))

def create_line(path: str, methods: List[str]) -> Generator[str, None, None]:
    keywords = get_keywords(path)
    operationId = get_configuration_id(path)
    strippedOperationId = operationId.upper()
    for keyword in keywords:
        strippedOperationId = strippedOperationId.replace(keyword.upper(), "BY_"+strip_brackets(keyword).upper())


    upper_methods = [method.upper() for method in methods]

    type_hint = f'Callable[[{", ".join(["str" for _ in keywords])}], str]' if keywords else 'str'

    typed_methods = [f"('{method}', {type_hint})" for method in upper_methods]

    cls = f'typing.NamedTuple("{strippedOperationId}", [{", ".join(typed_methods)}])'

    paths = [f"{method}={_create_line(path, operationId, keywords)}" for method in upper_methods]
    output = f"{strippedOperationId} = {cls}({', '.join(paths)})"
    return output

paths = json['paths']
print("import typing")
print("from typing import Callable")
for path in paths.keys():
    methods = json['paths'][path].keys()
    print(create_line(path, methods))


