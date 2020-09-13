# For this challenge,create a cone class that has two attributes:
#   *R=Radius
#   *h=Height
# And two methods:
#   *Volume = Π * r2 * (h/3)
#   *Surface area : base : Π * r2 , side : Π * r * √(r2 + h2)
# Make only one class with functions,as in where required import Math.
import math


class cone():
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        vol = math.pi*self.radius*self.radius*self.height*1/3
        return vol

    def surfaceArea(self):
        surfaceArea = math.pi*self.radius * \
            (self.radius+((self.radius**2)+(self.height**2)**1/2))
        return surfaceArea


p = cone(10, 10)
print(p.volume())
print(p.surfaceArea())
