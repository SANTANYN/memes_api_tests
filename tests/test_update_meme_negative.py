from data.api_json import ApiJson
from data.fake_data import FakeData, NegativeCases
from parametrization import Parametrization


class TestUpdateMemeNegative(FakeData, ApiJson):

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
    def test_update_meme_negative_test_for_info(self, login, create_and_delete, update_meme_by_id_api, info, expected):
        meme_id, payload_b = create_and_delete
        payload = ApiJson.update_meme_parametrized_json(meme_id, info, [f"{self.FAKE_WORD()}"], f"{self.FAKE_WORD()}",
                                                        f"{self.FAKE_WORD()}"
                                                        )
        update_meme_by_id_api.update_meme_endpoint(login, meme_id, payload)
        code = update_meme_by_id_api.get_status_code()
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
    def test_update_meme_negative_test_for_tags(self, login, update_meme_by_id_api, create_and_delete, tags, expected):
        meme_id, payload_b = create_and_delete
        payload = ApiJson.update_meme_parametrized_json(meme_id, {'colors': ['black']}, tags, f"{self.FAKE_WORD()}",
                                                        f"{self.FAKE_WORD()}"
                                                        )
        update_meme_by_id_api.update_meme_endpoint(login, meme_id, payload)
        code = update_meme_by_id_api.get_status_code()
        assert code == expected

    # тест не проходит с пустой строкой, длинной строкой, и с пробелами в строке, при создании это валидируется
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
    def test_update_meme_negative_test_for_text(self, login, update_meme_by_id_api, create_and_delete, text, expected):
        meme_id, payload_b = create_and_delete
        payload = ApiJson.update_meme_parametrized_json(meme_id, {'colors': ['black']}, ["test"], text,
                                                        f"{self.FAKE_WORD()}"
                                                        )
        update_meme_by_id_api.update_meme_endpoint(login, meme_id, payload)
        code = update_meme_by_id_api.get_status_code()
        assert code == expected

    # тест не проходит с пустой строкой, длинной строкой, и с пробелами в строке, при создании тоже есть проблема
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
    def test_update_meme_negative_test_for_url(self, login, update_meme_by_id_api, create_and_delete, url, expected):
        meme_id, payload_b = create_and_delete
        payload = ApiJson.update_meme_parametrized_json(meme_id, {'colors': ['black']}, ["test"], "test",
                                                        url
                                                        )
        update_meme_by_id_api.update_meme_endpoint(login, meme_id, payload)
        code = update_meme_by_id_api.get_status_code()
        assert code == expected
