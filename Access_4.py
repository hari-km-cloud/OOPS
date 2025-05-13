# inheritance Behaviour of derived class, called with object

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
    def __init__(self, name, area_of_expertise):
        PublicClass.__init__(self, name)
    
    def derived_public(x):
        return PublicClass().public(x)
   
    def _derived_protected(x):
        return PublicClass()._protected(x)
    
    def _derived_private(x):
        return PublicClass().__private(x)