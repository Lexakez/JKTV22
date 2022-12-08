from circle import circle
from math import pi

circle_list = []

with open("circles.txt", "r") as file:
    circ = file.readlines()
    for r in circ:
        circle_list.append(circle(int(r)))

for _ in circle_list:
    _.info()
