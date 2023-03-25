from unittest import TestCase
from io import StringIO

import os
import pytest


from tasks.file_filter import file_filter


class TestFileFilter(TestCase):
    def test_file_open(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, 'huge_file.txt')
        match_lines = file_filter(file_path, words=["роза"])

        self.assertEqual(next(match_lines), "Поиск должен выполняться по полному совпадению роза")
        self.assertEqual(next(match_lines), "Например, для строки из файла Роза упала")
        with pytest.raises(StopIteration):
            next(match_lines)

        match_lines = file_filter(file_path, words=[""])
        with pytest.raises(StopIteration):
            next(match_lines)

    def test_buffer_object(self):
        buffer = StringIO()
        buffer.write("buffer object\nOBJECT\ntest")
        match_lines = file_filter(buffer, words=["object", "test"])

        self.assertEqual(len(list(match_lines)), 3)

    def test_incorrect_file_objects(self):
        with pytest.raises(TypeError, match="File object must be path to file or StringIo object"):
            next(file_filter(123, words=[""]))
        with pytest.raises(FileNotFoundError):
            dir_path = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(dir_path, 'huge_file')
            next(file_filter(file_path, words=[""]))
