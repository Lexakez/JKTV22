from random import randint
import csv


'''
Первое задание
'''

# spisok = []
# for _ in range(5):
#     spisok.append(randint(0, 9))

# run = True

# while run:
#     print("1) Вывести все числа\n2) Добавить новое число\n3) Найти разницу между максимальным и минимальным значением")
#     choice = int(input("Выберите действие: "))
#     if choice == 1:
#         print(sorted(spisok))
#     elif choice == 2:
#         spisok.append(int(input("Введите новую цифру: ")))
#     elif choice == 3:
#         print(max(spisok) - min(spisok))
#     elif choice == 0:
#         run = False

'''
Второе задание
'''

# weather = {"Tallinn": "10",
#            "Tartu": "12",
#            "Jõhvi": "6",
#            "Kohtla-Järve": "9"}

# run = True

# while run:
#     print("1) Вывод всей информации о погоде.\n2) Поиск по введенному городу.\n3) Изменение температуры по указанному городу")
#     choice = int(input("Ввыберите действие из списка: "))
#     if choice == 1:
#         for i in weather:
#             print(f"{i}:  {weather[i]}")
#     elif choice == 2:
#         city = input("Выберите город: ")
#         print(f"Температура в {city}, {weather[city]} градусов")
#     elif choice == 3:
#         city = input("Введите город: ")
#         weather[city] = int(input("Введите новую температуру: "))
#     elif choice == 0:
#         run = False
        
# print(weather["Tartu"])

'''
Третье задание
'''

# a = int(input("Введите сторону прямоугольника: "))
# b = int(input("Введите вторую сторону прямоугольника: "))

# s = a * b
# p = (a * 2 + b * 2)

# with open("ristkulikud.txt","w") as file:
#     file.write(f"{a}|{b}|{s}|{p}")

'''
Четвертое задание
'''

# r = 0
# s = 0
# p = 0
# count = []
# with open("ringid.csv", "r", newline="") as file:
#     rings = csv.reader(file)
#     for circle in rings:
#         count.append(circle)
#         r += int(circle[0])
#         s += int(circle[1])
#         p += int(circle[2])
# print(f"Средний радиус: {round(r / len(count), 1)}\nСредняя площадь: {round(s / len(count), 1)}\nСредняя длинна окружности {round(p / len(count), 1)}")

'''
Пятое задание
'''

run = True
columns = ["Title","Author","Price"]

with open("knigi.csv", "r+", newline="") as file:
    reader = csv.DictReader(file, fieldnames = columns)
    dictwriter = csv.DictWriter(file, fieldnames = columns)
    

    while run:
        print("1) Вывод всей информации\n2) Поиск по части названия\n3) Поиск по автору\n4) Поиск в промежутке цен (от...до)\n5) Добавление в файл новой книги")
        choice = int(input("Выберите действие из списка: "))
        if choice == 1:
            for row in reader:
                print(f"Название: {row['Title']} \tАвтор: {row['Author']} \tЦена: {row['Price']}")
        if choice == 2:
            find = 0
            name = input("Введите название: ")
            for row in reader:
                if name in row['Title']:
                    find += 1
                    print(f"Название: {row['Title']} \tАвтор: {row['Author']} \tЦена: {row['Price']}")
            if find == 0:
                print("Название не найдено.")
        if choice == 3:
            find = 0
            name = input("Введите имя автора: ")
            for row in reader:
                if name in row['Author']:
                    find += 1
                    print(f"Название: {row['Title']} \tАвтор: {row['Author']} \tЦена: {row['Price']}")
            if find == 0:
                print("Автор не найден.")
        if choice == 4:
            find = 0
            mincena = int(input("Введите минимальную цену: "))
            maxcena = int(input("Введите максимальную цену: "))
            for row in reader:
                if float(row['Price']) >= mincena and float(row['Price']) <= maxcena:
                    find += 1
                    print(f"Название: {row['Title']} \tАвтор: {row['Author']} \tЦена: {row['Price']}")
            if find == 0:
                print("Совпадений не найдено.")
        if choice == 5:
            kniga = {"Title" : "", "Author" : "", "Price" : ""}
            kniga["Title"] = input("Введите название книги")
            kniga["Author"] = input("Введите автора книги")
            kniga["Price"] = input("Введите цену книги")
            dictwriter.writerow(kniga)
        if choice == 0:
            run = False








