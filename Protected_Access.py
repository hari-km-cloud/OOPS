# Scenario 1 : Outside class, function called using just the class name


'''
We check given public, private and protected functions of the same protected class, 
what is their scope outside the class and which of them are accessible under this scope.

'''

# same class without object

class _ProtectedClass:
	def __init__(self, name, area_of_expertise):
		self.name = name
		self._area_of_expertise = area_of_expertise
  
	def display_area_of_expertise_public(self):
	    print(self._area_of_expertise)

	def __display_area_of_expertise_private(self):
		print(self._area_of_expertise)

	def _display_area_of_expertise_protected(self):
		print(self._area_of_expertise)

	def _display_area_of_expertise(self):
		print(self._area_of_expertise)
  
	def display_public(x):
		y = x*3
		return y
	def _display_protected(x):
		y = x//3
		return y
	def __display_private(x):
		y = x//3
		return y

y = _ProtectedClass.display_public(7) # public fn of protected class
print(y)

# y = _ProtectedClass.__display_private(77) # private fn of protected class
# print(y)
# Gives Error : AttributeError: type object '_ProtectedClass' has no attribute '__display_private'

y = _ProtectedClass._display_protected(30) # protected fn of protected class
print(y)


# Scenario 2 : Using objects to access member function of protected class

obj1 = _ProtectedClass("Nemesis_1","python_public")
y = obj1.display_area_of_expertise_public() # public fn of protected class

# obj2 = _ProtectedClass("Nemesis","python_private")
# y = obj2.__display_area_of_expertise_private() # private instance method of protected class
# print(y)

# AttributeError: '_ProtectedClass' object has no attribute '__display_area_of_expertise_private'

obj3 = _ProtectedClass("Nemesis_1","python_protected")
y = obj3._display_area_of_expertise_protected() # protected instance method of protected class



# Scenario 3 : inheritance Behaviour of derived class, called without object

class DerivedClass(_ProtectedClass):
	def __init__(self, name, area_of_expertise):
		_ProtectedClass.__init__(name, area_of_expertise)

	def _display_area_of_expertise(self):
		return _ProtectedClass._display_area_of_expertise()

	def derived_public(x):
		return _ProtectedClass.display_public(x)

	def _derived_protected(x):
		return _ProtectedClass._display_protected(x)

	def __derived_private(x):
		return _ProtectedClass.__display_private(x)

y = DerivedClass.derived_public(7) # public fn of protected class
print(y)

# y = DerivedClass.__derived_private(77) # private fn of protected class
# print(y)

y = DerivedClass._derived_protected(30) # protected fn of protected class
print(y)

### Scenario 4 : inheritance Behaviour of derived class, called with object

class DerivedClass(_ProtectedClass):
	def __init__(self, name, area_of_expertise):
		_ProtectedClass.__init__(self, name, area_of_expertise)

	def _display_area_of_expertise(self):
		return _ProtectedClass._display_area_of_expertise()

	def derived_public(x):
		return _ProtectedClass.display_public(x)

	def _derived_protected(x):
		return _ProtectedClass._display_protected(x)

	def __derived_private(x):
		return _ProtectedClass.__display_private(x)

obj1 = DerivedClass("Nemesis_1","python_public")
y1 = obj1.display_area_of_expertise_public()

# obj2 = DerivedClass("Nemesis","python_private")
# y = obj2.__display_area_of_expertise_private() # private instance method of protected class
# print(y)


obj3 = DerivedClass("Nemesis_1","python_protected")
y = obj3._display_area_of_expertise_protected() # protected instance method of protected class


















