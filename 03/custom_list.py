from itertools import zip_longest


class CustomList(list):
    _comparing_error_msg = "Can only be compared with list or CustomList types"
    _add_error_msg = "Only list or CustomList can be stacked with each other"
    _sub_error_msg = "Only list or CustomList can be subtracted with each other"

    @staticmethod
    def _check_type(other, msg):
        if not isinstance(other, (list, CustomList)):
            raise TypeError(msg)

    def __eq__(self, other):
        CustomList._check_type(other, CustomList._comparing_error_msg)
        return sum(self) == sum(other) and len(self) == len(other) and all(self[i] == other[i]
                                                                           for i in range(len(self)))

    def __ne__(self, other):
        CustomList._check_type(other, CustomList._comparing_error_msg)
        return sum(self) != sum(other) or len(self) != len(other) or any(self[i] != other[i] for i in range(len(self)))

    def __lt__(self, other):
        CustomList._check_type(other, CustomList._comparing_error_msg)
        return sum(self) < sum(other)

    def __gt__(self, other):
        CustomList._check_type(other, CustomList._comparing_error_msg)
        return sum(self) > sum(other)

    def __le__(self, other):
        CustomList._check_type(other, CustomList._comparing_error_msg)
        return sum(self) <= sum(other)

    def __ge__(self, other):
        CustomList._check_type(other, CustomList._comparing_error_msg)
        return sum(self) >= sum(other)

    def __add__(self, other):
        CustomList._check_type(other, CustomList._add_error_msg)
        return CustomList([x + y for x, y in zip_longest(self, other, fillvalue=0)])

    def __radd__(self, other):
        CustomList._check_type(other, CustomList._add_error_msg)
        return CustomList.__add__(self, other)

    def __sub__(self, other):
        CustomList._check_type(other, CustomList._sub_error_msg)
        return CustomList([x - y for x, y in zip_longest(self, other, fillvalue=0)])

    def __rsub__(self, other):
        CustomList._check_type(other, CustomList._sub_error_msg)
        return CustomList([x - y for x, y in zip_longest(other, self, fillvalue=0)])

    def __str__(self):
        list_copy = self.copy()
        return f"{list_copy}, sum={sum(list_copy)}"
