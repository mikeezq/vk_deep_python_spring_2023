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

        assert self.positive_data.bin_num == "0b101101"
        assert self.positive_data.tern_num == "1200"
        assert self.positive_data.octal_num == "0o55"

    def test_negative_fields(self):
        assert self.negative_data.bin_num == "-0b101101"
        assert self.negative_data.tern_num == "-1200"
        assert self.negative_data.octal_num == "-0o55"

    def test_incorrect_values(self):
        with pytest.raises(AttributeError):
            Data("fake")
            Data([1, 2, 3])
