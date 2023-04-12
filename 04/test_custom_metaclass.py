from unittest import TestCase

import pytest

from custom_metaclass import CustomClass


class TestCustomMetaclass(TestCase):
    def setUp(self) -> None:
        self.custom_class_instance = CustomClass(1)

    def test_instance_fields(self):
        not_custom_attrs = ["test_attr", "val", "test_method"]
        with pytest.raises(KeyError):
            for not_custom_attr in not_custom_attrs:
                test = self.custom_class_instance.__dict__[not_custom_attr]

        self.custom_class_instance.new_val = 2
        with pytest.raises(AttributeError):
            test = self.custom_class_instance.new_val

        assert self.custom_class_instance.custom_new_val == 2
        assert self.custom_class_instance.custom_val == 1
        assert self.custom_class_instance.custom_test_method() == 10
        assert str(self.custom_class_instance) == "Custom_by_metaclass"

    def test_class_fields(self):
        CustomClass.new_field = 123
        with pytest.raises(AttributeError):
            test = CustomClass.test_attr
            test = CustomClass.new_field

        assert CustomClass.custom_test_attr == "test"
        assert CustomClass.custom_fake_field == 12345
        assert CustomClass.custom_new_field == 123

