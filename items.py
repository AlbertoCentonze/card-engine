class Property:
    def __init__(self, name, validator=None):
        self.name = name
        if validator is None:
            self.validate = lambda value: True
        elif isinstance(validator, list):
            def contains_element(x):
                return x in validator

            self.validate = contains_element
        elif callable(validator):
            self.validate = validator

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
