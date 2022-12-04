import re
import os
import requests
from typing import List, Generator, Callable, Union, Any, TypeVar, NamedTuple, Optional, Literal
from grocy.auth import APIKeyAuth
from dataclasses import dataclass, field

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
    return f'f"{path}"'


def _create_line(path: str, operationId: str, keywords: List[str]) -> Union[str, Callable]:
    if keywords:
        return (create_line_from_path(path, operationId, keywords))
    else:
        return (create_line_from_path(path))

def create_lines(path: str, methods: List[str]) -> Generator[str, None, None]:
    keywords = get_keywords(path)
    operationId = get_configuration_id(path)
    strippedOperationId = operationId.upper()
    for keyword in keywords:
        strippedOperationId = strippedOperationId.replace(keyword.upper(), "BY_"+strip_brackets(keyword).upper())


    upper_methods = [method.upper() for method in methods]
    
    lines = []
    indent = "    "

    lines += [f"class _{strippedOperationId}(NamedTuple):"]
    for method in upper_methods:
        lines += [f'{indent}def {method}({", ".join(["self"]+[strip_brackets(keyword)+": str" for keyword in keywords]+["**kwargs"])}):']
        lines += [f'{2*indent}return requests.Request("{method}", {create_line_from_path(path)}, **kwargs)']

    lines += [""]
    lines += [f"{strippedOperationId} = _{strippedOperationId}()"]
    lines += [""]
    lines += [""]
    
    return lines

Path = str
HTTPMethod = Literal['GET', 'PUT', 'POST', 'DELETE', 'OPTIONS', 'HEAD', 'PATCH', 'TRACE']

@dataclass
class OASOperationObject:
    method: HTTPMethod
    path: Path
    tags: List[str]
    components: dict[str, Any]
    summary: Optional[str] = None
    description: Optional[str] = None
    operationId: Optional[str] = None
    deprecated: Optional[bool] = None
    responses: Optional[Any] = None
    parameters: Optional[Any] = None
    requestBody: Optional[Any] = None

    _TypedDictDefinitions: List[str] = field(default_factory=list)

    def _clean_name(self, name: str) -> str:
        return name.strip("[]")

    def _resolve_ref(self, path: str):
        param = self.components
        for subpath in path.strip("#/").split("/"):
            param = param[subpath]
        return param

    def _schema_to_typehint(self, schema: dict, name: Optional[str]=None) -> str:
        if '$ref' in schema:
            refSchema = self._resolve_ref(schema["$ref"])
            return self._schema_to_typehint(refSchema, name=schema["$ref"].split("/")[-1])
        
        if 'oneOf' in schema:
            return f"Union[{', '.join([self._schema_to_typehint(one, name=name) for one in schema['oneOf']])}]"
                
        
        if 'type' not in schema:
            return "Any"

        schema_type = schema['type']
        if schema_type == "array":
            return f"List[{self._schema_to_typehint(schema['items'], name=name)}]"
        elif schema_type == 'string': 
            if 'enum' in schema:
                options = [f'"{option}"' for option in schema['enum']]
                return f"Literal[{', '.join(options)}]"
            return "str"
        elif schema_type == 'integer':
            return "int"
        elif schema_type == 'number':
            return "int"
        elif schema_type == 'boolean':
            return "bool"
        elif schema_type == 'object':
            if 'properties' in schema:
                props = {key: self._schema_to_typehint(value, name=name) for key, value in schema['properties'].items()}
                str_props = ", ".join([f"{key}={value}" for key, value in props.items()])
                self._TypedDictDefinitions += [f"{name} = TypedDict('{name}', {str_props})"]
                return name
            return "dict[str, Any]"
        return f"unkonwn_type_{schema_type}"

    def to_method(self) -> list[str]:
        query_params: List[str] = []
        parameter_descriptions: List[str] = []
        method_parameter_pairs: List[str] = []

        if (self.parameters):
            for param_entry in self.parameters:
                param = param_entry
                if '$ref' in param_entry:
                    param = self._resolve_ref(param_entry["$ref"])

                if 'schema' in param:
                    schema = param['schema']
                    name = self._clean_name(param['name'])
                    

                    required = param['required']
                    default_value = schema['default'] if 'default' in schema else None
                    postfix = f"={default_value}" if default_value else "=None" if not required else ""

                    method_parameter_pairs += [f"{name}: {self._schema_to_typehint(schema, name=name)}{postfix}"]
                    

                if 'in' in param:
                    if param['in'] == 'query':
                        query_params.append(param)

                if 'name' in param:
                    parameter_descriptions.append(f":param {self._clean_name(param['name'])}: {param['description'] if 'description' in param else ''}")
        
        body_type_hint = None
        if (self.requestBody):
            content = self.requestBody['content']
            required = self.requestBody['required'] if 'required' in self.requestBody else False
            schema = content['application/json']['schema'] if 'application/json' in self.requestBody['content'] else None
            if (schema):
                body_type_hint = self._schema_to_typehint(schema, name="Body")
                method_parameter_pairs += [f"body: {body_type_hint}"]


        method_signature = ", ".join(["cls"] + method_parameter_pairs)
        query_param_pairs = ", ".join([f"'{param['name']}': {self._clean_name(param['name'])}" for param in query_params]) if query_params else ""

        description_lines = [
            self.description
        ] if self.description else [] + parameter_descriptions

        

        kwargs = {
            'method': f"'{self.method}'",
            'url': f"f'{self.path}'",
            'params': "{"+query_param_pairs+"}" if query_param_pairs else None,  
        }
        if body_type_hint:
            kwargs['json'] = 'body'

        
        indent = "    "
        return self._TypedDictDefinitions + [
            "",
            f"@classmethod",
            f"def {self.method}({method_signature}) -> requests.Request:",] + ([
                indent+line for line in ['"""']+description_lines+['"""'] if line
            ] if description_lines else [])+[
            f"{indent}return requests.Request("
        ]+ [f"{2*indent}{k}={v}," for (k, v) in kwargs.items() if v is not None] + [
            f"{indent})" 
        ]


@dataclass
class OASPath:
    path: Path
    value: dict[HTTPMethod, OASOperationObject]

    def to_dataclass(self) -> list[str]:
        keywords = get_keywords(self.path)
        operationId = get_configuration_id(self.path)
        strippedOperationId = operationId.upper()
        for keyword in keywords:
            strippedOperationId = strippedOperationId.replace(keyword.upper(), "BY_"+strip_brackets(keyword).upper())
        
        newline = "\r\n"
        indent = "    "

        method_definitions = [f"{newline.join([indent+m for m in method.to_method() if m])}" for method in list(self.value.values())]

        return [
            "",
            f"class {strippedOperationId}:",
        ] + method_definitions



class OASSpec:
    def __init__(self, spec: dict[Path, dict[HTTPMethod, Any]]):
        self.specObj = spec
        self.parsedPaths = {
            path: OASPath(path, 
                {method.upper(): OASOperationObject(path=path, method=method.upper(), components=self.components(), **self.specObj['paths'][path][method]) for method in self.specObj['paths'][path].keys()}
            ) for path in self.specObj['paths']
        }
    def paths(self) -> list[OASPath]:
        return list(self.parsedPaths.values())

    def components(self):
        return self.specObj


    
class BaseGenerator:
    def __init__(self, spec: str, imports: List[str]):
        self.spec = OASSpec(spec)
        self.imports = imports
    
    def get_lines(self):
        for importstr in self.imports:
            yield importstr

        for path in self.spec.paths():
            for line in path.to_dataclass():
                yield line
            yield ""
        

    def render(self):
        raise NotImplementedError()


class ConsoleGenerator(BaseGenerator):
    def render(self):
        for line in self.get_lines():
            print(line)


class FileGenerator(BaseGenerator):
    def __init__(self, spec: str, imports: List[str], filePath: str):
        super().__init__(spec, imports)
        self.filePath = filePath

    def render(self):
        with open(self.filePath, 'w') as file:
            for line in self.get_lines():
                if (line is not None):
                    file.write(line + "\r\n")



generator = FileGenerator(json, ["import requests", "from typing import TypedDict, List, Any, Literal, Union"], "./grocy/pathsgen.py")

generator.render()
 