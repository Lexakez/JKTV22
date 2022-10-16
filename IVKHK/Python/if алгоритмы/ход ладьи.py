cell_column1 = int(input("Введите номер столбца первой клетки: "))
cell_line1 = int(input("Введите номер строки первой клетки: "))
cell_column2 = int(input("Введите номер столбца второй клетки: "))
cell_line2 = int(input("Введите номер строки второй клетки: "))

if cell_column1 > 8 or cell_line1 > 8 or cell_column2 > 8 or cell_line2 > 8:
    print("Не верные координаты")
elif cell_column1 <= 0 or cell_line1 <= 0 or cell_column2 <= 0 or cell_line2 <= 0:
    print("Не верные координаты")
else:
    if cell_column1 == cell_column2 or cell_line1 == cell_line2:
        print("Yes")
    else:
        print("No")