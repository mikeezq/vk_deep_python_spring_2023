import pytest

from custom_list import CustomList


@pytest.mark.parametrize(
    "subtraction,first_list,second_list,expected_sum,expected_list", [
        (False, CustomList([5, 1, 3, 7]), CustomList([1, 2, 7]), 26, CustomList([6, 3, 10, 7])),
        (False, CustomList([1, 2, 7]), CustomList([5, 1, 3, 7]), 26, CustomList([6, 3, 10, 7])),
        (False, CustomList([1]), [2, 5], 8, CustomList([3, 5])),
        (False, [2, 5], CustomList([1]), 8, CustomList([3, 5])),
        (False, CustomList([1, 1, 1]), CustomList([1, 1, 1]), 6, CustomList([2, 2, 2])),
        (True, CustomList([5, 1, 3, 7]), CustomList([1, 2, 7]), 6, CustomList([4, -1, -4, 7])),
        (True, CustomList([1, 2, 7]), CustomList([5, 1, 3, 7]), -6, CustomList([-4, 1, 4, -7])),
        (True, CustomList([2, 2, 2]), CustomList([1, 1, 1]), 3, CustomList([1, 1, 1])),
        (True, CustomList([1]), [2, 5], -6, CustomList([-1, -5])),
        (True, [2, 5], CustomList([1]), 6, CustomList([1, 5])),
    ]
)
def test_arithmetic_operations(subtraction, first_list, second_list, expected_sum, expected_list):
    if not subtraction:
        list_sum = first_list + second_list
    else:
        list_sum = first_list - second_list
    assert list_sum == [expected_sum]
    assert len(list_sum) == len(expected_list) and all(list_sum[i] == expected_list[i] for i in range(len(list_sum)))


def test_eq_ne():
    custom_list = CustomList([1, 2, 3])
    assert custom_list == CustomList([1, 2, 3, 0])
    assert custom_list == [6]

    assert custom_list != CustomList([1, 2, 2])
    assert custom_list != [5]


def test_lt_gt():
    custom_list = CustomList([1, 2, 3])
    assert custom_list > CustomList([1, 1, 1])
    assert custom_list > [1, 1, 1]
    assert not custom_list > CustomList([3, 3, 3])
    assert not custom_list > [3, 3, 3]

    assert custom_list < CustomList([3, 3, 3])
    assert custom_list < [3, 3, 3]
    assert not custom_list < CustomList([1, 1, 1])
    assert not custom_list < [1, 1, 1]


def test_le_ge():
    custom_list = CustomList([1, 2, 3])
    assert custom_list <= CustomList([1, 2, 3])
    assert custom_list <= [1, 2, 3]
    assert not custom_list <= CustomList([1, 1, 1])
    assert not custom_list <= [1, 1, 1]

    assert custom_list >= CustomList([1, 1, 1])
    assert custom_list >= [1, 1, 1]
    assert not custom_list >= CustomList([3, 3, 3])
    assert not custom_list >= [3, 3, 3]


def test_incorrect_operations():
    with pytest.raises(TypeError, match="Only list or CustomList can be stacked with each other"):
        assert CustomList([1, 2, 3]) + 1
        assert 1 + CustomList([1, 2, 3])

    with pytest.raises(TypeError, match="Only list or CustomList can be subtracted with each other"):
        assert CustomList([1, 2, 3]) - 1
        assert 1 - CustomList([1, 2, 3])

    with pytest.raises(TypeError, match="Can only be compared with list or CustomList types"):
        assert CustomList([1, 2, 3]) == 1
        assert CustomList([1, 2, 3]) != 1
        assert CustomList([1, 2, 3]) < 1
        assert CustomList([1, 2, 3]) > 1
        assert CustomList([1, 2, 3]) <= 1
        assert CustomList([1, 2, 3]) >= 1


def test_magic_str():
    assert str(CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7])) == "[6, 3, 10, 7], sum=26"
    assert f"{CustomList([1]) - [2, 5]}" == "[-1, -5], sum=-6"
