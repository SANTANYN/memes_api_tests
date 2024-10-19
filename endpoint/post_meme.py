import requests
from endpoint.base_api import BaseApi
from data.const import URL, MEME_POSTFIX, HEADER
from models.memes_response_model import MemeModel


class PostMeme(BaseApi):

    def post_meme_endpoint(self, token, payload):
        auth_header = {"Authorization": f"{token}"}
        self.response = requests.post(f'{URL}{MEME_POSTFIX}', json=payload, headers=auth_header)

    @property
    def data(self):
        return MemeModel(**self.response_json)

    def check_required_fields(self, payload):
        assert self.data.info == payload['info']
        assert self.data.text == payload['text']
        assert self.data.tags == payload['tags']
        assert self.data.url == payload['url']

    def check_id(self):
        resp_id = self.data.id
        assert resp_id is not None
        assert resp_id > 0

    def check_author(self):
        assert self.data.updated_by == 'santanyn'

    def check_check_that_url_is_link_in_body(self):
        assert "http" or 'https' in self.data.url

    def get_status_code(self):
        code = self.response.status_code
        return code
