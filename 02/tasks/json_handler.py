import json

from typing import List


def parse_json(json_str: str, keyword_callback, required_fields: List[str] = None, keywords: List[str] = None) -> json:
    try:
        f = json.loads(json_str)
    except json.decoder.JSONDecodeError:
        return None

    if not required_fields or not keywords:
        return f

    for key, value in f.items():
        if key in required_fields:
            f[key] = keyword_callback(value.split(), keywords)
    return f


def change_keywords(string_with_keywords: List[str], keywords: List[str]) -> str:
    for keyword in keywords:
        for index in range(len(string_with_keywords)):
            if string_with_keywords[index] == keyword:
                string_with_keywords[index] = "new_key"
    return " ".join(string_with_keywords)
