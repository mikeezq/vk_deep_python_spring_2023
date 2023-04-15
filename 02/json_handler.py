import json

from typing import List


def parse_json(json_str: str, keyword_callback, required_fields: List[str] = None, keywords: List[str] = None) -> json:
    try:
        f_json = json.loads(json_str)
    except json.decoder.JSONDecodeError:
        return None

    if not required_fields or not keywords or not keyword_callback:
        return f_json

    for key, _ in f_json.items():
        if key in required_fields:
            for word in f_json[key].split():
                if word in keywords:
                    keyword_callback(key, word)
    return f_json


def change_keywords(required_field: str, keyword: str) -> str:
    return f"{required_field} + {keyword}"


def change_keywords2(required_field: str, keyword: str) -> str:
    return f"{required_field} + {keyword}"
