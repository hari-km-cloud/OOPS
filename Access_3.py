#  inheritance — Behaviour of derived class, called without object -

# Derived class cann't access private members of Base class

class PublicClass:
    def __init__(self, name = "your name"):
        self.name = name

    def public(self, x):
        y = str(x*3) + ":" + self.name
        return y

    def _protected(self, x):
        y = str(x//3) + ":" + self.name
        return y

    def __private(self, x):
        y = str(x) + 3 + ":" + self.name
        return y


class DerivedClass(PublicClass):
    def __init__(self, name):
        PublicClass.__init__(self, name)

    def display_derived(self):
        return self.name


obj1 = DerivedClass("Phillips")
y = obj1.display_derived() # public fn of public class
print(y)

obj3 = DerivedClass("Nemesis_1")
y = obj3._protected(10) # protected instance method of public class
print(y)

# obj2 = DerivedClass("Darry")
# y = obj2.__private(30) # private instance method of public class
# print(y)

# # Output : AttributeError: 'DerivedClass' object has no attribute '__private'


# # miscellaneous

# # obj4 = DerivedClass("Gucci", "Perfume")
# # obj4.display_area_of_expertise()
# # print(obj4.name)
# # print(obj4.multiply_by_3(10)) # so you cant do this as the first argument in this call is self, but this is not a object method.