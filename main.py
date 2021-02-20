# Name - Sirpreet Padda
# Class - MCSCI - 270
# Due date - 04/20/2020
# Title - TestCircle


import math


class Circle:

    # Construct a circle object
    def __init__(self, radius=1):
        self.radius = radius

    def getPerimeter(self):
        return 2 * self.radius * math.pi

    def getArea(self):
        return self.radius * self.radius * math.pi

    def setRadius(self, radius):
        self.radius = radius


def main():
    # Create a circle with radius 1
    circle1 = Circle(float(1))
    print("The area of the circle of radius",
          circle1.radius, "is", circle1.getArea())

    # Create a circle with radius 25
    circle2 = Circle(float(25))
    print("The area of the circle of radius",
          circle2.radius, "is", circle2.getArea())

    # Create a circle with radius 125
    circle3 = Circle(float(125))
    print("The area of the circle of radius",
          circle3.radius, "is", circle3.getArea())

    # Modify circle radius
    circle2.radius = float(100)
    print("The area of the circle of radius",
          circle2.radius, "is", circle2.getArea())


# Call the main function
main()
