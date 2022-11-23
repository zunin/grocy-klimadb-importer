import requests
import os

class APIKeyAuth(requests.auth.AuthBase):
    def __call__(self, r: requests.request):
        r.headers['GROCY-API-KEY'] = os.environ['GROCY_API_KEY']
        return r
