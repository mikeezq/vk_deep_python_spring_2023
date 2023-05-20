#! /usr/bin/env python3

import json
import pytest


from json_handler import loads, dumps


def test_convert_json():
    json_str = '{"str": 1234, "a": "b"}'
    expected_dict = {"str": 1234, "a": "b"}

    cpy_dict = loads(json_str)
    assert cpy_dict == expected_dict == json.loads(json_str)

    cpy_json_str = dumps(cpy_dict)
    assert cpy_json_str == json_str
    assert json_str == json.dumps(cpy_dict)


def test_incorrect_json():
    json_str = '{"str":1234,"a":"b"'
    with pytest.raises(ValueError, match="Invalid JSON string: Unterminated value"):
        loads(json_str)
