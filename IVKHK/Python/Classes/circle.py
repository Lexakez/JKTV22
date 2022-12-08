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