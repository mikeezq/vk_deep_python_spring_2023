class BaseDescriptor:
    def __set_name__(self, owner, name):
        self._instance_attr_name = f"_int_field_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return

    def __set__(self, obj, val):
        if obj is None:
            return

        if not isinstance(val, int):
            raise AttributeError(f"{val=} is not an integer!")

        return setattr(obj, self._instance_attr_name, val)

    def __delete__(self, obj):
        if obj is None:
            return

        return delattr(obj, self._instance_attr_name)


class Binary(BaseDescriptor):
    def __get__(self, instance, owner):
        super().__get__(instance, owner)
        return bin(getattr(instance, self._instance_attr_name))


class Ternary(BaseDescriptor):
    def __get__(self, instance, owner):
        super().__get__(instance, owner)
        num = getattr(instance, self._instance_attr_name)
        return change_notation(num, 3)


class Octal(BaseDescriptor):
    def __get__(self, instance, owner):
        super().__get__(instance, owner)
        return oct(getattr(instance, self._instance_attr_name))


def change_notation(num, base):
    if num == 0:
        ternary = "0"
    else:
        ternary = ""
        positive_num = abs(num)
        while positive_num > 0:
            remainder = positive_num % base
            ternary = str(remainder) + ternary
            positive_num = positive_num // base
        if num < 0:
            ternary = "-" + ternary
    return ternary


class Data:
    bin_num = Binary()
    tern_num = Ternary()
    octal_num = Octal()

    def __init__(self, val):
        self.bin_num = val
        self.tern_num = val
        self.octal_num = val
