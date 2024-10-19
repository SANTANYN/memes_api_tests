import requests
from endpoint.base_api import BaseApi
from data.const import URL, MEME_POSTFIX
from models.memes_response_model import DeleteMemeModel


class DeleteMemeById(BaseApi):

    def delete_meme_endpoint(self, token, meme_id):
        auth_header = {"Authorization": f"{token}"}
        self.response = requests.delete(f'{URL}/{MEME_POSTFIX}/{meme_id}', headers=auth_header)
        print(self.response.text)

    @property
    def data(self):
        return DeleteMemeModel(**self.response_json)

