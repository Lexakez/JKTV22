from circle import circle, cylinder
from math import pi

circle_list = []
cylinder_list = []

with open("circles.txt", "r") as file:
    circ = file.readlines()
    for r in circ:
        circle_list.append(circle(int(r)))

cylinder_list.append(cylinder(int(10), int(10)))

for _ in circle_list:
    _.info()

for _ in cylinder_list:
    _.info()