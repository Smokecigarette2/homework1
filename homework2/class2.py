class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length ** 2



shape1 = Shape()
print(shape1.area())
shape2 = Square(2)
print(shape2.area())