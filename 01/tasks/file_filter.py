from io import StringIO
from typing import List, Generator


def find_matches(line: str, words: List[str]) -> bool:
    line_words = line.strip().lower().split()
    for word in words:
        if word in line_words:
            return True
    return False


def file_filter(file_object: [str, StringIO], words: List[str]) -> Generator[str, str, None]:
    if isinstance(file_object, str):
        with open(file_object, "r", encoding="UTF-8") as file:
            for line in file:
                if find_matches(line, words):
                    yield line.strip()
    elif isinstance(file_object, StringIO):
        file_object.seek(0)
        for line in file_object:
            if find_matches(line, words):
                yield line.strip()
    else:
        raise TypeError("File object must be path to file or StringIo object")
