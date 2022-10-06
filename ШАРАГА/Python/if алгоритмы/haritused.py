'''
Первое задание
'''

# number = input("Введите число от 100 до 999: ")

# if number[0] == "1":
#     n1 = "Сто"
# elif number[0] == "2":
#     n1 = "Двести"
# elif number[0] == "3":
#     n1 = "Триста"
# elif number[0] == "4":
#     n1 = "Четыреста"
# elif number[0] == "5":
#     n1 = "Пятьсот"
# elif number[0] == "6":
#     n1 = "Шестьсот"
# elif number[0] == "7":
#     n1 = "Семьсот"
# elif number[0] == "8":
#     n1 = "Восемьсот"
# elif number[0] == "9":
#     n1 = "Девятьсот"

# if number[1] == "1":
#     if number[2] == "0":
#         n2 = "десять"
#     elif number[2] == "1":
#         n2 = "одинадцать"
#     elif number[2] == "2":
#         n2 = "двенадцать"
#     elif number[2] == "3":
#         n2 = "тринадцать"
#     elif number[2] == "4":
#         n2 = "четырнадцать"
#     elif number[2] == "5":
#         n2 = "пятнадцать"
#     elif number[2] == "6":
#         n2 = "шестьнадцать"
#     elif number[2] == "7":
#         n2 = "семьнадцать"
#     elif number[2] == "8":
#         n2 = "восемнадцать"
#     elif number[2] == "9":
#         n2 = "девятнадцать"
# elif number[1] == "2":
#     n2 = "двадцать"
# elif number[1] == "3":
#     n2 = "тридцать"
# elif number[1] == "4":
#     n2 = "сорок"
# elif number[1] == "5":
#     n2 = "пятьсот"
# elif number[1] == "6":
#     n2 = "шестьсот"
# elif number[1] == "7":
#     n2 = "семьдесят"
# elif number[1] == "8":
#     n2 = "восемьдесят"
# elif number[1] == "9":
#     n2 = "девяноста"

# if number[2] == "0":
#     n3 = ""
# elif number[2] == "1":
#     n3 = "один"
# elif number[2] == "2":
#     n3 = "два"
# elif number[2] == "3":
#     n3 = "три"
# elif number[2] == "4":
#     n3 = "четыри"
# elif number[2] == "5":
#     n3 = "пять"
# elif number[2] == "6":
#     n3 = "шесть"
# elif number[2] == "7":
#     n3 = "семь"
# elif number[2] == "8":
#     n3 = "восемь"
# elif number[2] == "9":
#     n3 = "девять"


# print(f"{n1} {n2} {n3}")

'''
Второе задание
'''

day = int(input("Введите день своего рождения: "))
month = int(input("Введите месяц своего рождения: "))

if month == 1 and day in range(20, 31) or month == 2 and day in range(1, 18):
    print("Водолей")
elif month == 2 and day in range(19, 28) or month == 3 and day in range(1, 20):
    print("Рыбы")
elif month == 3 and day in range(21, 31) or month == 4 and day in range(1, 19):
    print("Овен")
elif month == 4 and day in range(20, 30) or month == 5 and day in range(1, 20):
    print("Телец")
elif month == 5 and day in range(21, 31) or month == 6 and day in range(1, 21):
    print("Близнецы")
elif month == 6 and day in range(22, 30) or month == 7 and day in range(1, 23):
    print("Рак")
elif month == 7 and day in range(24, 31) or month == 8 and day in range(1, 22):
    print("Лев")
elif month == 8 and day in range(23, 31) or month == 9 and day in range(1, 22):
    print("Дева")
elif month == 9 and day in range(23, 30) or month == 10 and day in range(1, 22):
    print("Весы")
elif month == 10 and day in range(23, 31) or month == 11 and day in range(1, 22):
    print("Скорпион")
elif month == 11 and day in range(23, 30) or month == 12 and day in range(1, 21):
    print("Стрелец")
elif month == 12 and day in range(22, 31) or month == 1 and day in range(1, 19):
    print("Козерог")
    

