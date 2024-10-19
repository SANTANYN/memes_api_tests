import requests
from endpoint.base_api import BaseApi
from data.const import URL, AUTHORIZATION_POSTFIX, HEADER
from models.memes_response_model import MemeModel


class GetAuthTokenStatus(BaseApi):

    def get_auth_token_status(self, token):
        self.response = requests.get(f'{URL}{AUTHORIZATION_POSTFIX}/{token}', headers=HEADER)

    @property
    def data(self):
        return MemeModel(**self.response_json)

    def check_token(self):
        assert self.response.text == 'Token is alive. Username is santanyn'