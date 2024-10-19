import requests
from endpoint.base_api import BaseApi
from data.const import URL, MEME_POSTFIX
from models.memes_response_model import MemeModel


class PutMeme(BaseApi):

    def update_meme_endpoint(self, token, meme_id, payload):
        auth_header = {"Authorization": f"{token}"}
        self.response = requests.put(f"{URL}{MEME_POSTFIX}/{meme_id}", json=payload, headers=auth_header)

    @property
    def data(self):
        return MemeModel(**self.response_json)

    def check_that_all_fields_are_updated(self, old_body):
        assert self.data.url != old_body['url']
        assert self.data.text != old_body['text']
        assert self.data.tags != old_body['tags']
        assert self.data.info != old_body['info']

    def check_that_id_are_same(self, old_body):
        assert self.data.id == old_body['id']

    def check_that_author_are_correct(self):
        assert self.data.updated_by == "santanyn"

    def get_status_code(self):
        code = self.response.status_code
        return code

