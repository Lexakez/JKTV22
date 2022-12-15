from rect import Rect

rectangles = [Rect(2, 3), Rect(1, 5), Rect(5, 2)]

rectangles.append(Rect(int(input("Введите сторону а: ")), int(input("Введите сторону b: "))))
for _ in rectangles:
    _.info()