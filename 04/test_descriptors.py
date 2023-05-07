from unittest import TestCase

import pytest

from descriptors import Data


class TestDescriptors(TestCase):
    def setUp(self):
        self.positive_data = Data(45)
        self.negative_data = Data(-45)

    def test_positive_fields(self):
        attributes = {'_int_field_bin_num': 45,
                      '_int_field_tern_num': 45,
                      '_int_field_octal_num': 45
                      }
        assert attributes == self.positive_data.__dict__

        assert self.positive_data.bin_num == 101101
        assert self.positive_data.tern_num == 1200
        assert self.positive_data.octal_num == 55

        with pytest.raises(AttributeError, match="val='string' is not an integer!"):
            self.positive_data.bin_num = "string"
        assert self.positive_data.bin_num == 101101

        self.positive_data.bin_num = 12345
        assert self.positive_data.bin_num == 11000000111001

        self.positive_data.tern_num = 12345
        assert self.positive_data.tern_num == 121221020

        self.positive_data.octal_num = 12345
        assert self.positive_data.octal_num == 30071

    def test_negative_fields(self):
        assert self.negative_data.bin_num == -101101
        assert self.negative_data.tern_num == -1200
        assert self.negative_data.octal_num == -55

        with pytest.raises(AttributeError, match="val='string' is not an integer!"):
            self.positive_data.bin_num = "string"
        assert self.negative_data.bin_num == -101101

        self.negative_data.bin_num = -12345
        assert self.negative_data.bin_num == -11000000111001

        self.negative_data.tern_num = -12345
        assert self.negative_data.tern_num == -121221020

        self.negative_data.octal_num = -12345
        assert self.negative_data.octal_num == -30071

    def test_incorrect_values(self):
        with pytest.raises(AttributeError):
            Data("fake")
            Data([1, 2, 3])

        with pytest.raises(AttributeError, match="val='string' is not an integer!"):
            self.positive_data = Data("string")
