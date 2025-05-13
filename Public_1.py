# same class without object

#Outside class, function called using just the class name

class PublicClass:
    def __init__(self, name = "default_name", area_of_expertise = "default area of expertise"):
        self.name = name
        self.area_of_expertise = area_of_expertise

    def display_area_of_expertise(self):
        print(self.area_of_expertise)

    def multiply_by_3(x):
        y = x*3
        return y

    def _divide_by_3(x):
        y = x//3
        return y

    def __add_3(x):
        y = x+3
        return y

# y = multiply_by_3(7)
# print(y)

y1 = PublicClass.multiply_by_3(7) # public function of public class
print(y1)

# y2 = PublicClass.__add_3(77) # private function of public class
# print(y2)

y3 = PublicClass._divide_by_3(30) # protected function of public class
print(y3)