from functools import reduce


class Property:
    def __init__(self, name, validator=None, types=None):
        self.name = name  # TODO remove name and extract it from the attribute
        # validating function
        if validator is None:
            def validate(x):
                return True
        elif isinstance(validator, list):
            def validate(x):
                return x in validator
        elif callable(validator):
            def validate(x):
                return validator()
        else:
            raise TypeError()

        # type validation function
        if types is None:
            def type_validate(_type):
                return True
        elif isinstance(types, list):
            def type_validate(_type):
                return _type in types
        else:
            raise TypeError()

        self.validator = lambda arg: validate(arg) and type_validate(type(arg))

    def __repr__(self) -> str:
        return f"Property {self.name}"


def constructor_factory(cls):
    props_name_list = [prop.name for prop in cls.props]

    def __init__(self, **kwargs):
        undefined_props = list(cls.props)
        for key, value in kwargs.items():
            for prop in undefined_props:
                if key in props_name_list and prop.validate(value):
                    setattr(self, key, value)
                    undefined_props.remove(prop)
                elif key not in props_name_list:
                    raise Exception("key not in item")
                elif not prop.validate(value):
                    raise Exception(f"{prop.name}'s value does not respect conditions")

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
                cls.props.append(val)

        # props from inherited classes TODO

        for prop in cls.props:
            setattr(cls, prop.name, "value")
        setattr(cls, "__init__", constructor_factory(cls))


Item = ItemMetaclass("Item", (), {})
