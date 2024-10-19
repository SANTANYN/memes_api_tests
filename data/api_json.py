from data.fake_data import FakeData


class ApiJson:

    @staticmethod
    def auth_api_json():
        payload = {"name": "santanyn"}
        return payload

    @staticmethod
    def create_meme_json():
        payload = {
            "info": {
                "colors": [
                    f"{FakeData.FAKE_COLOR()}",
                    f"{FakeData.FAKE_COLOR()}",
                    f"{FakeData.FAKE_COLOR()}"
                ],
                "objects": [
                    f"{FakeData.FAKE_WORD()}",
                    f"{FakeData.FAKE_WORD()}"
                ]
            },
            "tags": [f"{FakeData.random_tags()}"],
            "text": f"{FakeData.FAKE_SENTENCE(nb_words=5)}",
            "url": f"{FakeData.FAKE_IMAGE_URL()}"
        }
        return payload

    @staticmethod
    def create_meme_parametrized_json(info, tags, text, url):
        payload = {
            "info": info,
            "tags": tags,
            "text": text,
            "url": url
        }
        return payload

    @staticmethod
    def update_meme_json(meme_id):
        payload = {
            "id": meme_id,
            "info": {
                "colors": [
                    f"{FakeData.FAKE_COLOR()}",
                    f"{FakeData.FAKE_COLOR()}",
                    f"{FakeData.FAKE_COLOR()}"
                ],
                "objects": [
                    f"{FakeData.FAKE_WORD()}",
                    f"{FakeData.FAKE_WORD()}"
                ]
            },
            "tags": [f"{FakeData.random_tags()}"],
            "text": f"{FakeData.FAKE_SENTENCE(nb_words=5)}",
            "url": f"{FakeData.FAKE_IMAGE_URL()}"
        }
        return payload

    @staticmethod
    def update_meme_parametrized_json(meme_id, info, tags, text, url):
        payload = {
            "id": meme_id,
            "info": info,
            "tags": tags,
            "text": text,
            "url": url
        }
        return payload
