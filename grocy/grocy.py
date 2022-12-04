import requests
import os
from auth import APIKeyAuth
import pathsgen as paths
from pathsgen import OBJECTS_BY_ENTITY
Product = OBJECTS_BY_ENTITY.Product


def grocy_request(request: requests.Request, **kwargs):
    request.url = f"{os.environ['GROCY_API_URI']}{request.url}"
    request.auth = APIKeyAuth()
    session = requests.Session()

    return session.send(request.prepare(), **kwargs)


req = grocy_request(paths.OBJECTS_BY_ENTITY.POST("products", Product()))
req.raise_for_status()
print(req.json())
