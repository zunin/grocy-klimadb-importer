import requests
import os
from typing import Union
from auth import APIKeyAuth
import paths



def grocy_request(method: str, url: str, **kwargs):
    return requests.request(method, f"{os.environ['GROCY_API_URI']}{url}", auth=APIKeyAuth(), **kwargs)


req = grocy_request("GET", paths.BATTERIES.GET)
req.raise_for_status()
print(req.json())
