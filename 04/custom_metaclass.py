class CustomMeta(type):
    def override_setattr(cls, key, value):
        if not (key.startswith("__") and key.endswith("__")):
            key = f"custom_{key}"
            cls.__dict__[key] = value

    @classmethod
    def override_dict(mcs, class_dict):
        custom_class_dict = {}
        for key, value in class_dict.items():
            if not (key.startswith("__") and key.endswith("__")):
                custom_class_dict[f"custom_{key}"] = value
            else:
                custom_class_dict[key] = value
        return custom_class_dict

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):  # pylint: disable=W0613
        return {"test_attr": "test"}

    def __init__(cls, name, bases, class_dict, **kwargs):
        super().__init__(name, bases, class_dict, **kwargs)

    def __new__(mcs, name, bases, class_dict, **kwargs):
        custom_class_dict = mcs.override_dict(class_dict)
        custom_class_dict["__setattr__"] = mcs.override_setattr

        cls = super().__new__(mcs, name, bases, custom_class_dict)

        return cls

    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        instance.__dict__ = cls.override_dict(instance.__dict__)

        return instance

    def __setattr__(cls, key, value):
        if not (key.startswith("__") and key.endswith("__")):
            key = f"custom_{key}"
            super().__setattr__(key, value)
        else:
            super().__setattr__(key, value)


class CustomClass(metaclass=CustomMeta):
    fake_field = 12345

    def __init__(self, val):
        self.val = val

    def test_method(self):
        return 10

    def __str__(self):
        return "Custom_by_metaclass"

