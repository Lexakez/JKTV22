from math import pi
class circle:
    def __init__(self, r):
        self.r = r

    def circleL(self):
        return 2 * pi * self.r
    
    def circleS(self):
        return pi * (self.r ** 2)

    def info(self):
        print(f"Circle {self.r} S = {self.circleS()} L = {self.circleL()}")

class cylinder(circle):
    def __init__(self, r, h):
        circle.__init__
        self.r = r
        self.h = h
    def cylinderS(self):
        return self.circleS() * 2 + self.circleL() * self.h
    # def cylinderV(self)
    def info(self):
        print(f"Cylinder {self.r}, {self.h} S = {self.cylinderS()}")
