class Point:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def show(self):
        return self.coordinates

    def move(self, new_coordinates):
        self.coordinates = new_coordinates
    def dist(self, another_point):

        return (self.coordinates[0] - another_point.coordinates[0])**2 + (self.coordinates[1] - another_point.coordinates[1])**2


point1 = Point([1,2])
print(point1.show())
point1.move([2,4])
print(point1.show())
point2 = Point([3,6])

print(point1.dist(point2))