import csv

andmed = [
    {"x": 0, "y": 0},
    {"x": 1, "y": 2},
    {"x": 3, "y": 4},
    {"x": 5, "y": 6},
]
with open("andmed.csv", "w", newline="") as file:
    columns = ["x", "y"]
    wr = csv.DictWriter(file, fieldnames = columns)
    wr.writeheader()
    wr.writerows(andmed)

with open("andmed.csv", "r", newline = "") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["x"], "-", row["y"])