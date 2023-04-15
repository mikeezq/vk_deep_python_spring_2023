import json
import functools

from unittest import TestCase
from faker import Faker
from mock import patch

from json_handler import parse_json


class TestJsonHandler(TestCase):
    def test_parse_calls(self):
        json_str = '{"keyword1": "cat dog bad", "keyword2": "cat dog test"}'

        with patch("json_handler.change_keywords") as mock_changer:
            parse_json_call = functools.partial(parse_json, json_str, mock_changer)
            parse_json_call(["keyword1", "keyword2"], ["cat", "test"])
            parse_json_call(["keyword1"], ["cat"])
            parse_json_call(["keyword2"], ["cat"])
            parse_json_call(["keyword2"], ["fake"])

            expected_calls1 = [("keyword1", "cat"), ("keyword2", "cat"), ("keyword2", "test"),
                               ("keyword1", "cat"),
                               ("keyword2", "cat")]

            i = 0
            for call in mock_changer.call_args_list:
                for args in call:
                    if args:
                        assert args == expected_calls1[i]
                        i += 1
            assert mock_changer.call_count == 5

        json_sets = fake_jsons()
        with patch("json_handler.change_keywords") as mock_changer:
            for json_set in json_sets:
                parse_json(json.dumps(json_set), mock_changer, ["name"], ["test"])
            self.assertEqual(mock_changer.call_count, 100)

        with patch("json_handler.change_keywords2") as mock_changer:
            parse_json_call = functools.partial(parse_json, json_str, mock_changer)
            parse_json_call(["keyword1", "keyword2"], ["cat", "test"])
            parse_json_call(["keyword1"], ["cat"])

            assert mock_changer.call_count == 4

    @patch("json_handler.change_keywords")
    def test_incorrect_jsons(self, mock_changer):
        self.assertIsNone(parse_json("", mock_changer))
        self.assertIsNone(parse_json('{"keyword1": "cat}', mock_changer))
        self.assertIs(mock_changer.called, False)
        self.assertEqual(parse_json('{"keyword1": "cat"}', None, [], []), {"keyword1": "cat"})
        self.assertEqual(parse_json('{"keyword1": "cat"}', mock_changer, None), {"keyword1": "cat"})
        self.assertEqual(parse_json('{"keyword1": "cat"}', mock_changer, ["some_key"], None), {"keyword1": "cat"})


def fake_jsons():
    fake = Faker(locale="Ru_ru")
    json_sets = []
    for _ in range(100):
        doc = {
            'name': 'test',
            'address': fake.address(),
            'company': fake.company(),
            'country': fake.country(),
            'text': fake.sentence()
        }
        json_sets.append(doc)
    return json_sets
