# function to extract the values of a dict into a list using list comprehension
from typing import Callable, Any

class PropertyConditionNotMet(Exception):
	pass
class PropertyConditionTypeError(TypeError):
	pass

class Property: 
	def __init__(self, prop_type: type, name: str, condition: Callable[[Any], bool] = None): # type: ignore
		self.type = prop_type
		self.name = name
		self.condition = condition if condition else lambda x : True # type: ignore

	def create(self, value: Any, name: str) -> type:
		if type(value) is not self.type:
			raise TypeError(f"Property is not of type {self.type}")
		try:
			if not self.condition(value): # type: ignore
				raise PropertyConditionNotMet(f"Property is not of type {self.type}")
		except TypeError:
			raise PropertyConditionTypeError(f"This condition cannot be checked on type {self.type}")

		return type(name.capitalize(), (), {})
	
	@staticmethod
	def from_list(list: list[Any], prop_type: type, name: str) -> "Property":
		# check that all the elements in the list are of type prop_type
		for element in list:
			if type(element) is not prop_type:
				raise PropertyConditionTypeError(f"Property is not of type {prop_type}")
		condition = lambda x : x in list 
		return Property(prop_type, name, condition)


