from unittest import TestCase

import pytest

from typing import List, Dict

from custom_list import CustomList


class TestCustomList(TestCase):
    def test_compare_operations(self):
        test_lists = [CustomList([1, 2, 3, 4]), [1, 2, 3, 4]]

        custom_list = CustomList([4, 5])
        ops = {'<': True, '<=': True, '==': False, '!=': True, '>': False, '>=': False}
        assert_expressions(custom_list, test_lists, ops)

        custom_list = CustomList([4, 5, 6, 7])
        ops = {'<': False, '<=': False, '==': False, '!=': True, '>': True, '>=': True}
        assert_expressions(custom_list, test_lists, ops)

        assert CustomList([1, 2, 3, 4]) == CustomList([1, 2, 3, 4])
        assert CustomList([5, 5]) != CustomList([1, 2, 3, 4])

        incorrect_value = 123
        with pytest.raises(TypeError, match="Can only be compared with list or CustomList types"):
            for op in ops:
                expr = f"custom_list {op} incorrect_value"
                assert eval(expr)

    def test_arithmetic_operations(self):
        cl_1, cl_2 = CustomList([5, 1, 3, 7]), CustomList([1, 2, 7])
        assert cl_1 + cl_2 == CustomList([6, 3, 10, 7])
        assert CustomList([5, 1, 3, 7]), CustomList([1, 2, 7]) == (cl_1, cl_2)

        assert CustomList([1]) + [2, 5] == CustomList([3, 5])
        assert [2, 5] + CustomList([1]) == CustomList([3, 5])

        assert CustomList([5, 1, 3, 7]) - CustomList([1, 2, 7]) == CustomList([4, -1, -4, 7])
        assert CustomList([1]) - [2, 5] == CustomList([-1, -5])
        assert [2, 5] - CustomList([6, 2]) == CustomList([-4, 3])

    def test_magic_str(self):
        assert str(CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7])) == "[6, 3, 10, 7], sum=26"
        assert "{}".format(CustomList([1]) - [2, 5]) == "[-1, -5], sum=-6"


def assert_expressions(custom_list: CustomList, test_lists: List, ops: Dict) -> None:
    """
    Asserts that a given CustomList object passes a series of comparison tests using
    the specified operators and test lists.

    Args:
    custom_list (CustomList): The CustomList object to be tested.
    test_lists (list): A list of lists to compare with the CustomList object.
    ops (dict): A dictionary of comparison operators and their expected boolean results.

    Raises:
    AssertionError: If any of the evaluated expressions do not match the expected result.
    """
    for test_list in test_lists:
        for op, ans in ops.items():
            expr = f"custom_list {op} test_list"
            assert eval(expr) == ans
