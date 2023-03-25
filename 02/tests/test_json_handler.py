import json
import functools

from unittest import TestCase
from faker import Faker
from mock import patch

from tasks.json_handler import parse_json, change_keywords


class TestJsonHandler(TestCase):
    def test_parse_calls(self):
        json_str = '{"keyword1": "cat dog bad", "keyword2": "cat dog test"}'
        expected_json = {"keyword1": "cat new_key bad", "keyword2": "cat new_key new_key"}

        parse_json_call = functools.partial(parse_json, json_str, change_keywords)
        json_json = json.loads(json_str)

        self.assertEqual(parse_json_call(["keyword1", "keyword2"], ["dog", "test"]), expected_json)
        self.assertEqual(parse_json_call(), json_json)
        self.assertEqual(parse_json_call([], ["dog"]), json_json)
        self.assertEqual(parse_json_call(["keyword"], []), json_json)

        json_sets = fake_jsons()
        with patch("tasks.json_handler.change_keywords") as mock_changer:
            for json_set in json_sets:
                parse_json(json.dumps(json_set), mock_changer, ["name"], ["test_test"])
            self.assertEqual(mock_changer.call_count, 100)

    @patch("tasks.json_handler.change_keywords")
    def test_incorrect_jsons(self, mock_changer):
        self.assertIsNone(parse_json("", mock_changer))
        self.assertIsNone(parse_json('{"keyword1": "cat}', mock_changer))
        self.assertIs(mock_changer.called, False)


def fake_jsons():
    fake = Faker(locale="Ru_ru")
    json_sets = []
    for i in range(100):
        doc = {
            'name': fake.name(),
            'address': fake.address(),
            'company': fake.company(),
            'country': fake.country(),
            'text': fake.sentence()
        }
        json_sets.append(doc)
    return json_sets
