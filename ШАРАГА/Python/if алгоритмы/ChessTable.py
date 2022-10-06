cell_column1 = int(input("Введите номер столбца первой клетки: "))
cell_line1 = int(input("Введите номер строки первой клетки: "))
cell_column2 = int(input("Введите номер столбца второй клетки: "))
cell_line2 = int(input("Введите номер строки второй клетки: "))

#  1 = черный цвет, 0 = белый цвет клетки

if (cell_line1 + cell_column1) % 2 == 0:
    colour_1 = 1
elif (cell_line1 + cell_column1) % 2 == 1:
    colour_1 = 0

if (cell_line2 + cell_column2) % 2 == 0:
    colour_2 = 1
elif (cell_line2 + cell_column2) % 2 == 1:
    colour_2 = 0

print(colour_1, colour_2)

if colour_1 == colour_2:
    print("YES")
else:
    print("NO")
    
    
    
    
    
