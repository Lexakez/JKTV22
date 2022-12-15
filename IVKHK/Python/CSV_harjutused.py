import csv
from math import *

rows = int(input("Введите количество строк: "))

numbers = []


print(numbers)

with open("points.csv", "w", newline="") as file:
    for num in range(rows):
        numbers.append({"x": "", "y":""})
        numbers[num]["x"] = input("X:")
        numbers[num]["y"] = input("y:")
    columns = ["x", "y"]
    dictwriter = csv.DictWriter(file, fieldnames = columns)
    dictwriter.writeheader()
    dictwriter.writerows(numbers)
with open("points.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    points = []
    for row in reader:
        points.append((int(row["x"]),int(row["y"])))
    suma = 0
    for point in range(len(points) - 1):
        suma += sqrt((points[point][0] - points[point + 1][0]) ** 2 + (points[point][1] - points[point + 1][1]) ** 2)
    
    print(suma)
