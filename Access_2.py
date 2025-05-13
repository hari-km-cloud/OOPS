#Using object of class to call function

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


obj1 = PublicClass("Public")
obj1.public(30) # public function of public class
print(obj1.name)


# obj2 = PublicClass("Private")
# y2 = obj2.__private() # private instance method of protected class
# print(y2)

# # Output : 'PublicClass' object has no attribute '__private'

obj3 = PublicClass("Protected")
y3 = obj3._protected(20) # protected instance method of protected class

print(y3)