import requests
from endpoint.base_api import BaseApi
from data.const import URL, MEME_POSTFIX
from models.memes_response_model import MemesResponseModel


class GetMemes(BaseApi):

    def get_memes_endpoint(self, token):
        auth_header = {"Authorization": f"{token}"}
        self.response = requests.get(f'{URL}{MEME_POSTFIX}', headers=auth_header)

    @property
    def data(self):
        return MemesResponseModel(**self.response_json)

    def check_response_body_is_not_empty(self):
        assert self.data.json() != {}

