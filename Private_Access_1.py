#Scenario 1 : Outside class, function called using just the class name


class __PrivateClass:
    def __init__(self, name, area_of_expertise):
        self.name = name
        self.__area_of_expertise = area_of_expertise

    def __display_private(self):
        print("Inside private function")
        print(self.__area_of_expertise)
    
    def display_public(self):
        print("Inside public function")
        self.__display_private()
    
    def __func_private_multiply(x):
        y = x*3
        return y
    
    def func_public(x):
        return x*3

    def _func_protected(x):
        y = x//3
        return y
    def __func_private_devide(x):
        y = x//3
        return y

class DerivedClass(__PrivateClass):
    def __init__(self, name, area_of_expertise):
        __PrivateClass.__init__(name, area_of_expertise)

    def display_area_of_expertise_from_derived_class(self):
        print(self.display_public())

    def derived_private(x):
        y = __PrivateClass.__func_private_devide(x) #internally calls private function
        return y

    def derived_public(x):
        y = __PrivateClass.func_public(x) #internally calls public function
        return y

    def derived_public(x):
        return __PrivateClass.func_public(x)

    def _derived_protected(x):
        return __PrivateClass._func_protected(x)

    def __derived_private(x):
        return __PrivateClass.__func_private_devide(x)


################## Using Class ###############################
y = __PrivateClass.func_public(7) # public fn of private class
print(y)
# y = __PrivateClass.__func_private_devide(77)
# print(y)
y = __PrivateClass._func_protected(30)
print(y)



###################### Using Object ##########################

y = __PrivateClass('Phillips', "Cricketer")
y.display_public()

# obj3 = __PrivateClass("MS","Cricketer")
# y = obj3.__display_private()

#AttributeError: '__PrivateClass' object has no attribute '__display_private'


##  inheritance behaviour of derived class and objects of derived class ##


# obj1 = DerivedClass("Sam","Cricketer")
# y = obj1.display_public() # public instance fn of private class

# Output : NameError: name '_DerivedClass__PrivateClass' is not defined

# obj2 = DerivedClass("Curan","Football")
# y = obj2.__display_private() # private instance method of private class
# print(y)

# # Output : AttributeError: 'DerivedClass' object has no attribute 'display_public'

# obj3 = DerivedClass("Bilings","Protected")
# y = obj3._display_area_of_expertise_protected() # protected instance method of private class

#'_DerivedClass__PrivateClass' is not defined