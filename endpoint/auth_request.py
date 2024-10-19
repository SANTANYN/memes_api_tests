import requests
from endpoint.base_api import BaseApi
from data.const import URL, AUTHORIZATION_POSTFIX, HEADER
from models.auth_api_model import AuthApiResponse


class AuthRequest(BaseApi):

    def auth_request_endpoint(self, payload):
        self.response = requests.post(f'{URL}{AUTHORIZATION_POSTFIX}', json=payload, headers=HEADER)

    @property
    def data(self):
        return AuthApiResponse(**self.response_json)

