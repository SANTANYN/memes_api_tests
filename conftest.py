import pytest
from endpoint.auth_request import AuthRequest
from endpoint.get_memes import GetMemes
from endpoint.get_meme_by_id import GetMemesById
from endpoint.post_meme import PostMeme
from endpoint.delete_memes import DeleteMemeById
from endpoint.update_meme import PutMeme
from endpoint.get_token_status import GetAuthTokenStatus
from data.api_json import ApiJson


@pytest.fixture(scope='session')
def login(auth_api):
    payload = ApiJson.auth_api_json()
    auth_api.auth_request_endpoint(payload)
    return auth_api.data.token


@pytest.fixture(scope='function')
def create_and_delete(login, post_meme_api, delete_meme_by_id_api):
    payload = ApiJson.create_meme_json()
    post_meme_api.post_meme_endpoint(login, payload)
    meme_id = post_meme_api.data.id
    yield meme_id, payload
    delete_meme_by_id_api.delete_meme_endpoint(login, meme_id)


@pytest.fixture(scope="session")
def auth_api():
    return AuthRequest()


@pytest.fixture(scope="session")
def get_auth_token_status_api():
    return GetAuthTokenStatus()


@pytest.fixture(scope="session")
def get_memes_api():
    return GetMemes()


@pytest.fixture(scope="session")
def get_meme_by_id_api():
    return GetMemesById()


@pytest.fixture(scope="session")
def post_meme_api():
    return PostMeme()


@pytest.fixture(scope="session")
def delete_meme_by_id_api():
    return DeleteMemeById()


@pytest.fixture(scope="session")
def update_meme_by_id_api():
    return PutMeme()
