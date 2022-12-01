import csv

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
    pointlist=[]
    point = ()
    for row in reader:
        x = row["x"]
        y = row["y"]
        pointlist.append(point(row["x"],row["y"]))
        # print(rows["x"], "-", rows["y"])


