import random

from locust import HttpUser, task
from data.const import URL, MEME_POSTFIX


class MemeSeeker(HttpUser):
    token: str

    @task(50)
    def get_publication(self, login, meme_id):
        headers = {'Authorization': login}
        meme_id = random.randrange(1, 509)
        self.client.get(f'{URL}{MEME_POSTFIX}/{meme_id}', headers=headers)
