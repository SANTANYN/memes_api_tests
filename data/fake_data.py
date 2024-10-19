from faker import Faker
import random


class FakeData:

    fake = Faker()
    FAKE_FIRST_NAME = fake.first_name
    FAKE_LAST_NAME = fake.last_name
    FAKE_SENTENCE = fake.sentence
    FAKE_JOB = fake.job
    FAKE_WORD = fake.word
    FAKE_INT = fake.random_int
    FAKE_FUTURE_DATE = fake.future_date
    FAKE_DATE = fake.date
    FAKE_IMAGE_URL = fake.image_url
    FAKE_COLOR = fake.color_name

    @staticmethod
    def random_tags():
        fake = Faker()
        tags = [fake.word(), fake.word(), fake.word(), "pepa", "monkey", "fat_cat", "cat"]
        number_of_tags = random.choice([1, 7])
        result = random.sample(tags, number_of_tags)
        return result


class NegativeCases(FakeData):
    EMPTY_STRING = ""
    VERY_LONG_STRING = "test" * 300
    STRING_SPACE = "    "
    SYMBOL_IN_STRING = "!@#$%^*&^ SELECT *"
    TOO_HEAVY_INTEGER = 99999999999999999999999999999999999999999999
    ZERO = 0
    NEGATIVE_NUMBER = -99999
    FLOAT = 3.14159265
    BOOL_TRUE = True
    BOOL_FALSE = False
    NONE = None
    OBJECT = {}
    LIST = []
