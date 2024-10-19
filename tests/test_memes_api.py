from data.api_json import ApiJson


class TestMeme:

    def test_auth_token_status(self, login, get_auth_token_status_api):
        get_auth_token_status_api.get_auth_token_status(login)
        get_auth_token_status_api.check_token()

    def test_get_memes(self, login, get_memes_api):
        get_memes_api.get_memes_endpoint(login)
        get_memes_api.check_response_code_is_(200)
        get_memes_api.check_response_body_is_not_empty()

    def test_create_meme(self, login, post_meme_api):
        payload = ApiJson.create_meme_json()
        post_meme_api.post_meme_endpoint(login, payload)
        post_meme_api.check_response_code_is_(200)
        post_meme_api.check_required_fields(payload)
        post_meme_api.check_check_that_url_is_link_in_body()
        post_meme_api.check_id()
        post_meme_api.check_author()

    def test_get_meme_by_id(self, login, get_meme_by_id_api, create_and_delete):
        meme_id, payload = create_and_delete
        get_meme_by_id_api.get_meme_by_id_endpoint(login, meme_id)
        get_meme_by_id_api.check_response_code_is_(200)
        get_meme_by_id_api.check_response_body_is_not_empty()
        get_meme_by_id_api.check_fields(payload)

    def test_update_meme_by_id(self, login, create_and_delete, update_meme_by_id_api):
        meme_id, payload_before_update = create_and_delete
        payload_for_update = ApiJson.update_meme_json(meme_id)
        update_meme_by_id_api.update_meme_endpoint(login, meme_id, payload_for_update)
        update_meme_by_id_api.check_that_all_fields_are_updated(payload_before_update)
        update_meme_by_id_api.check_that_author_are_correct()

    def test_delete_object_by_id(self, login, post_meme_api, delete_meme_by_id_api, get_meme_by_id_api):
        payload = ApiJson.create_meme_json()
        post_meme_api.post_meme_endpoint(login, payload)
        post_meme_api.check_response_code_is_(200)
        meme_id = post_meme_api.data.id
        delete_meme_by_id_api.delete_meme_endpoint(login, meme_id)
        get_meme_by_id_api.get_meme_by_id_endpoint(login, meme_id)
        get_meme_by_id_api.check_response_code_is_(404)

    def test_and2and_memes_api(self, login,
                               post_meme_api,delete_meme_by_id_api, get_meme_by_id_api, update_meme_by_id_api):
        payload = ApiJson.create_meme_json()
        post_meme_api.post_meme_endpoint(login, payload)
        post_meme_api.check_response_code_is_(200)
        post_meme_api.check_required_fields(payload)
        post_meme_api.check_check_that_url_is_link_in_body()
        post_meme_api.check_id()
        post_meme_api.check_author()
        meme_id = post_meme_api.data.id
        get_meme_by_id_api.get_meme_by_id_endpoint(login, meme_id)
        get_meme_by_id_api.check_response_code_is_(200)
        get_meme_by_id_api.check_response_body_is_not_empty()
        get_meme_by_id_api.check_fields(payload)
        payload_for_update = ApiJson.update_meme_json(meme_id)
        update_meme_by_id_api.update_meme_endpoint(login, meme_id, payload_for_update)
        update_meme_by_id_api.check_that_all_fields_are_updated(payload)
        update_meme_by_id_api.check_that_author_are_correct()
        delete_meme_by_id_api.delete_meme_endpoint(login, meme_id)
        get_meme_by_id_api.get_meme_by_id_endpoint(login, meme_id)
        get_meme_by_id_api.check_response_code_is_(404)





