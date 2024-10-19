from data.api_json import ApiJson
from data.fake_data import FakeData, NegativeCases
from parametrization import Parametrization


class TestCreateMemeNegative(FakeData, ApiJson):

    @Parametrization.parameters("info", "expected")
    @Parametrization.case("EMPTY_STRING", NegativeCases.EMPTY_STRING, 400)
    @Parametrization.case("VERY_LONG_STRING", NegativeCases.VERY_LONG_STRING, 400)
    @Parametrization.case("STRING_SPACE", NegativeCases.STRING_SPACE, 400)
    @Parametrization.case("TOO_HEAVY_INTEGER", NegativeCases.TOO_HEAVY_INTEGER, 400)
    @Parametrization.case("ZERO", NegativeCases.ZERO, 400)
    @Parametrization.case("NEGATIVE_NUMBER", NegativeCases.NEGATIVE_NUMBER, 400)
    @Parametrization.case("FLOAT", NegativeCases.FLOAT, 400)
    @Parametrization.case("BOOL_TRUE", NegativeCases.BOOL_TRUE, 400)
    @Parametrization.case("BOOL_FALSE", NegativeCases.BOOL_FALSE, 400)
    @Parametrization.case("NONE", NegativeCases.NONE, 400)
    @Parametrization.case("LIST", NegativeCases.LIST, 400)
    def test_create_meme_negative_test_for_info(self, login, post_meme_api, info, expected):
        payload = ApiJson.create_meme_parametrized_json(info, [f"{self.FAKE_WORD()}"], f"{self.FAKE_WORD()}",
                                                        f"{self.FAKE_WORD()}"
                                                        )
        post_meme_api.post_meme_endpoint(login, payload)
        code = post_meme_api.get_status_code()
        assert code == expected

    @Parametrization.parameters("tags", "expected")
    @Parametrization.case("EMPTY_STRING", NegativeCases.EMPTY_STRING, 400)
    @Parametrization.case("VERY_LONG_STRING", NegativeCases.VERY_LONG_STRING, 400)
    @Parametrization.case("STRING_SPACE", NegativeCases.STRING_SPACE, 400)
    @Parametrization.case("TOO_HEAVY_INTEGER", NegativeCases.TOO_HEAVY_INTEGER, 400)
    @Parametrization.case("ZERO", NegativeCases.ZERO, 400)
    @Parametrization.case("NEGATIVE_NUMBER", NegativeCases.NEGATIVE_NUMBER, 400)
    @Parametrization.case("FLOAT", NegativeCases.FLOAT, 400)
    @Parametrization.case("BOOL_TRUE", NegativeCases.BOOL_TRUE, 400)
    @Parametrization.case("BOOL_FALSE", NegativeCases.BOOL_FALSE, 400)
    @Parametrization.case("NONE", NegativeCases.NONE, 400)
    @Parametrization.case("LIST", NegativeCases.OBJECT, 400)
    def test_create_meme_negative_test_for_tags(self, login, post_meme_api, tags, expected):
        payload = ApiJson.create_meme_parametrized_json({'colors': ['black']}, tags, f"{self.FAKE_WORD()}",
                                                        f"{self.FAKE_WORD()}"
                                                        )
        post_meme_api.post_meme_endpoint(login, payload)
        code = post_meme_api.get_status_code()
        assert code == expected

    @Parametrization.parameters("text", "expected")
    @Parametrization.case("EMPTY_STRING", NegativeCases.EMPTY_STRING, 400)
    @Parametrization.case("VERY_LONG_STRING", NegativeCases.VERY_LONG_STRING, 400)
    @Parametrization.case("STRING_SPACE", NegativeCases.STRING_SPACE, 400)
    @Parametrization.case("TOO_HEAVY_INTEGER", NegativeCases.TOO_HEAVY_INTEGER, 400)
    @Parametrization.case("ZERO", NegativeCases.ZERO, 400)
    @Parametrization.case("NEGATIVE_NUMBER", NegativeCases.NEGATIVE_NUMBER, 400)
    @Parametrization.case("FLOAT", NegativeCases.FLOAT, 400)
    @Parametrization.case("BOOL_TRUE", NegativeCases.BOOL_TRUE, 400)
    @Parametrization.case("BOOL_FALSE", NegativeCases.BOOL_FALSE, 400)
    @Parametrization.case("NONE", NegativeCases.NONE, 400)
    @Parametrization.case("object", NegativeCases.OBJECT, 400)
    @Parametrization.case("list", NegativeCases.LIST, 400)
    def test_create_meme_negative_test_for_text(self, login, post_meme_api, text, expected):
        payload = ApiJson.create_meme_parametrized_json({'colors': ['black']}, ['test'], text, f"{self.FAKE_WORD()}")
        post_meme_api.post_meme_endpoint(login, payload)
        code = post_meme_api.get_status_code()
        assert code == expected

    # тест не проходит с пустой строкой, длинной строкой, и с пробелами в строке, это мем апи, так что -
    # ссылка должна быть обязательной, длина ссылки 1500 это перебор, и так же в ней не должно быть пробелов
    @Parametrization.parameters("url", "expected")
    @Parametrization.case("EMPTY_STRING", NegativeCases.EMPTY_STRING, 400)
    @Parametrization.case("VERY_LONG_STRING", NegativeCases.VERY_LONG_STRING, 400)
    @Parametrization.case("STRING_SPACE", NegativeCases.STRING_SPACE, 400)
    @Parametrization.case("TOO_HEAVY_INTEGER", NegativeCases.TOO_HEAVY_INTEGER, 400)
    @Parametrization.case("ZERO", NegativeCases.ZERO, 400)
    @Parametrization.case("NEGATIVE_NUMBER", NegativeCases.NEGATIVE_NUMBER, 400)
    @Parametrization.case("FLOAT", NegativeCases.FLOAT, 400)
    @Parametrization.case("BOOL_TRUE", NegativeCases.BOOL_TRUE, 400)
    @Parametrization.case("BOOL_FALSE", NegativeCases.BOOL_FALSE, 400)
    @Parametrization.case("NONE", NegativeCases.NONE, 400)
    @Parametrization.case("LIST", NegativeCases.OBJECT, 400)
    @Parametrization.case("list", NegativeCases.LIST, 400)
    def test_create_meme_negative_test_for_url(self, login, post_meme_api, url, expected):
        payload = ApiJson.create_meme_parametrized_json({'colors': ['black']}, ['test'], f"{self.FAKE_WORD()}", url)
        post_meme_api.post_meme_endpoint(login, payload)
        code = post_meme_api.get_status_code()
        assert code == expected
