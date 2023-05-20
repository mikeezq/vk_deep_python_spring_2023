#! /usr/bin/env python3

import cjson


def loads(json_str):
    py_dict = cjson.loads(json_str)
    return py_dict


def dumps(py_dict):
    json_str = cjson.dumps(py_dict)
    return json_str
