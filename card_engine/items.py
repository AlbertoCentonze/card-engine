import inspect


class Property:
    def __init__(self, validator=None, types=None):
        # validating function
        if validator is None:
            def validate(x):
                return True
        elif isinstance(validator, list):
            def validate(x):
                return x in validator
        elif callable(validator):
            def validate(x):
                return validator
        else:
            raise TypeError()

        # type validation function
        # if types is None:
        #     def type_validate(_type):
        #         return True
        # elif isinstance(types, list):
        #     def type_validate(_type):
        #         return _type in types
        # else:
        #     raise TypeError()

        self.validator = lambda arg: validate(arg)  # and type_validate(type(arg))


def constructor_factory(cls):
    prop_names_list = []
    for key, prop in cls.props:
        prop_names_list.append(key)

    def __init__(self, **kwargs):
        undefined_props = list(prop_names_list)
        for key, value in kwargs.items():
            if key in prop_names_list and cls.props[key].validator(value):
                setattr(self, key, value)
                undefined_props.remove(prop)
            elif key not in prop_names_list:
                raise Exception(f"key: {key} not in item")
            elif not prop.validator(value):
                raise Exception(f"value {value} does not respect {key} conditions")

    return __init__


class ItemMetaclass(type):
    def __init__(cls, name, bases, attrs):
        # calling the method from type to make the class behave normally
        super(ItemMetaclass, cls).__init__(name, bases, attrs)

        # storing all the props here
        cls.props = []

        # props from attrs
        for key, val in attrs.items():
            if isinstance(val, Property):
                cls.props.append((key, val))

        # props from inherited classes TODO

        for key, prop in cls.props:
            setattr(cls, key, None)
        setattr(cls, "__init__", constructor_factory(cls))


Item = ItemMetaclass("Item", (), {})
