class shape:
    def calculate_area(self):
        pass


class rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)


def calculate_totalarea(shapes):
    totalarea = 0
    for shapes in shapes:
        totalarea += shape.calculate_area()


mycircle = circle(9)
myrectangle = rectangle(5, 6)

print(f"The ara of the circle is {mycircle.calculate_area()} "
      f"and the area of the rectangle is {myrectangle.calculate_area()}")
