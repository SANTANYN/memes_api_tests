import requests
from endpoint.base_api import BaseApi
from data.const import URL, MEME_POSTFIX
from models.memes_response_model import MemeModel


class GetMemesById(BaseApi):

    def get_meme_by_id_endpoint(self, token, meme_id):
        auth_header = {"Authorization": f"{token}"}
        self.response = requests.get(f'{URL}{MEME_POSTFIX}/{meme_id}', headers=auth_header)

    @property
    def data(self):
        return MemeModel(**self.response_json)

    def check_response_body_is_not_empty(self):
        assert self.data.json() != {}

    def check_fields(self, payload):
        assert self.data.info == payload['info']
        assert self.data.tags == payload['tags']
        assert self.data.text == payload['text']
        assert self.data.url == payload['url']
