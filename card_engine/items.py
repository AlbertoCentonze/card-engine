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
                return validator(x)
        else:
            raise TypeError()

        # type validation function
        if types is None:
            def validate_type(_type):
                return True
        elif isinstance(types, list):
            def validate_type(_type):
                return _type in types
        else:
            raise ValueError("types expects a list of types or None")

        self.validator = lambda arg: validate_type(type(arg)) and validate(arg)


def constructor_factory(cls):
    prop_names_list = []
    for key, prop in cls.props:
        prop_names_list.append(key)

    def __init__(self, *args, **kwargs):
        for key, _ in kwargs.items():
            if key not in prop_names_list:
                raise AttributeError(f"argument key {key} is not contained in the properties of the class (check the "
                                     f"names of kwargs)")
        if len(args) > 0:
            raise AttributeError("You should pass the parameters specifying their name (ex. param=5) and not as a "
                                 "positional argument")
        if len(kwargs) != len(prop_names_list):
            raise AttributeError("Wrong number of parameters passed to item constructor")

        for prop_key, prop_value in cls.props:
            for arg_key, arg_value in kwargs.items():
                if prop_key == arg_key:
                    if prop_value.validator(arg_value):
                        setattr(self, arg_key, arg_value)
                    elif arg_key not in prop_names_list:
                        raise AttributeError(f"key: {key} not in item")
                    elif not prop_value.validator(arg_value):
                        raise AttributeError(f"value \"{arg_value}\" does not respect {key} conditions or types")

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
            setattr(cls, f"_{key}", None)
        setattr(cls, "__init__", constructor_factory(cls))
        setattr(cls, "__repr__", lambda self: "item")  # TODO better repr


Item = ItemMetaclass("Item", (), {})
