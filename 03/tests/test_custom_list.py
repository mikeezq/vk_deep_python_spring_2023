from unittest import TestCase

import pytest

from tasks.custom_list import CustomList


class TestCustomList(TestCase):
    def test_compare_operations(self):
        test_lists = [CustomList([1, 2, 3, 4]), [1, 2, 3, 4]]

        custom_list = CustomList([4, 5, 6])
        ops = {'<': True, '<=': True, '==': False, '!=': True, '>': False, '>=': False}
        assert_expressions(custom_list, test_lists, ops)

        custom_list = CustomList([4, 5, 6, 7])
        ops = {'<': False, '<=': True, '==': True, '!=': False, '>': False, '>=': True}
        assert_expressions(custom_list, test_lists, ops)

        incorrect_value = 123
        with pytest.raises(TypeError, match="Can only be compared with list or CustomList types"):
            for op in ops:
                expr = f"custom_list {op} incorrect_value"
                assert eval(expr)

    def test_arithmetic_operations(self):
        self.assertEqual(CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7]), CustomList([6, 3, 10, 7]))
        self.assertEqual(CustomList([1]) + [2, 5], CustomList([3, 5]))
        self.assertEqual([2, 5] + CustomList([1]), CustomList([3, 5]))

        self.assertEqual(CustomList([5, 1, 3, 7]) - CustomList([1, 2, 7]), CustomList([4, -1, -4, 7]))
        self.assertEqual(CustomList([1]) - [2, 5], CustomList([-1, -5]))
        self.assertEqual([2, 5] - CustomList([1]), CustomList([1, 5]))

    def test_magic_str(self):
        self.assertEqual(str(CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7])), "[6, 3, 10, 7], sum=26")
        self.assertEqual("{}".format(CustomList([1]) - [2, 5]), "[-1, -5], sum=-6")


def assert_expressions(custom_list, test_lists, ops):
    for test_list in test_lists:
        for op, ans in ops.items():
            expr = f"custom_list {op} test_list"
            assert eval(expr) == ans
