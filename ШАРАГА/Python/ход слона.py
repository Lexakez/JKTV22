

cell_column1 = int(input("Введите номер столбца первой клетки: "))
cell_line1 = int(input("Введите номер строки первой клетки: "))
cell_column2 = int(input("Введите номер столбца второй клетки: "))
cell_line2 = int(input("Введите номер строки второй клетки: "))

if abs(cell_column2 - cell_column1) == abs(cell_line2 - cell_line1):
    print("Yes")
else:
    print("No")
