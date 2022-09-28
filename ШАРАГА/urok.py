from math import *


'''
Первое задание.
'''
# number  = int(input("Enter the day of week: "))

# if number >= 1 and number <= 7:
#     if number == 1:
#         print("monday")
#     elif number == 2:
#         print("tuesday")
#     elif number == 3:
#         print("wednesday")
#     elif number == 4:
#         print("thursday")
#     elif number == 5:
#         print("friday")
#     elif number == 6:
#         print("saturday")
#     elif number == 7:
#         print("sunday")
# else:
#     print("Invalid")

'''
Второе задание
'''

# month = int(input("Enter number of month: "))

# if month >= 1 and month <= 12:
#     if month >= 3 and month <= 5:
#         print("spring")
#     elif month >= 6 and  month <= 8:
#         print("summer")
#     elif month >= 9 and month <= 11:
#         print("autumn")
#     else:
#         print("winter")
# else:
#     print("Error")
'''
Третье задание
'''


# km = int(input("Введите расстояние в километрах: "))

# fut = float(input("Введите расстояние в футах: "))

# km_v_m = km * 1000

# fut_v_m = float(fut) * 0.348

# if km_v_m > fut_v_m:
#     print(f"{km} километров больше чем {int(fut)} футов")
# elif km_v_m < fut_v_m:
#     print(f"{km} километров меньше чем {int(fut)} футов")
# else:
#     print(f"{km} километров равна {int(fut)} футов")
'''
Четвертое задание
'''
# number = int(input("Введи двух значное чилсо: "))

# if len(str(number)) == 2:
#     if number // 10 > number % 10:
#         print(f"Цифра: {number // 10} больше чем: {number % 10}")
#     elif number // 10 < number % 10:
#         print(f"Цифра: {number // 10} меньше чем: {number % 10}")
#     else:
#         print(f"Цифра {number // 10} равна цифре: {number % 10}")
#     if number // 10 + number % 10 < 10:
#         print(f"Сумма этих цифр равна: {number // 10 + number % 10} что являеться однозначным числом")
#     elif number // 10 + number % 10 > 10:
#         print(f"Сумма этих цифр равна: {number // 10 + number % 10} что являеться двухзначным числом")
#     if number // 10 == 3 or number % 10 == 3:
#         print(f"Число {number} содержит цифру 3")
#     else:
#         print(f"Число {number} не содержит цифру 3")
# else:
#     print("Error")

'''
Пятое задание
'''

# ticket = input("Введите номер своего билета(6 цифр): ")
# if len(str(ticket)) == 6:
#     if (int(ticket[0]) + int(ticket[1]) + int(ticket[2])) == (int(ticket[3]) + int(ticket[4]) + int(ticket[5])):
#         print("У вас счастливый билет!!!")
#     else:
#         print("У вас вполне обычный билет")
# else:
#     print("Не правильный номер билета")

'''
второй вариант
'''


# if len(str(ticket)) == 6:
#     t1 = ticket // 100000
#     t2 = (ticket % 100000) // 10000
#     t3 = (ticket % 10000) // 1000
#     t4 = (ticket % 1000) // 100
#     t5 = (ticket % 100) // 10
#     t6 = ticket % 10
#     #print(t1, t2, t3, t4, t5, t6)
#     if t1 + t2 + t3 == t4 + t5 + t6:
#         print("У вас счастливый билет!!!")
#     else:
#         print("У вас вполне обычный билет")
# else:
#     print("Не правильный номер билета")

'''
Шестое задание
'''
pol = input("Введите пол (m/n)")
voz = int(input("Введите свой возраст: "))
rost = int(input("Введите свой рост: "))
mass = int(input("Введите свой вес: "))

if pol.lower() == "m" or pol.lower() == "м":
    mass_id = (3 * rost - 450 + voz) * 0.25 + 45.5
    zhir_protsent = (mass - mass_id) / mass * 100 + 15
    mass_ind = mass / (rost / 100) ** 2
    p = 8.9 * zhir_protsent + 11 * (100 - zhir_protsent)
    objom = 1000 * mass / p
    y = (35.75 - log(mass, 10))
    s = ((1000 * mass) ** y) * rost ** 0.3
    if mass_ind < 18:
        print("kõhn")
        print(f"Идеальный вес: {round(mass_id, 1)}")
        print(f"Индекс массы тела: {round(mass_ind, 1)}")
        print(f"Процент жира: {round(zhir_protsent, 1)}")
    elif 18 <= mass_ind <= 25:
        print("normaal")
        print(f"Идеальный вес: {round(mass_id, 1)}")
        print(f"Индекс массы тела: {round(mass_ind, 1)}")
        print(f"Процент жира: {round(zhir_protsent, 1)}")
    elif 25 < mass_ind <= 30:
        print("ulekaal")
        print(f"Идеальный вес: {round(mass_id, 1)}")
        print(f"Индекс массы тела: {round(mass_ind, 1)}")
        print(f"Процент жира: {round(zhir_protsent, 1)}")
    elif mass_ind > 30:
        print("ei voi olla!")

elif pol.lower() == "n" or pol.lower() == "ж":
    mass_id = (3 * rost - 450 + voz) * 0.225 + 45.5
    zhir_protsent = (mass - mass_id) / mass * 100 + 22
    mass_ind = mass / (rost / 100) ** 2
    p = 8.9 * zhir_protsent + 11 * (100 - zhir_protsent)
    objom = 1000 * mass / p
    y = (35.75 - log(mass, 10))
    s = ((1000 * mass) ** y) * rost ** 0.3
    if mass_ind < 18:
        print("kõhn")
        print(f"Идеальный вес: {round(mass_id, 1)}")
        print(f"Индекс массы тела: {round(mass_ind, 1)}")
        print(f"Процент жира: {round(zhir_protsent, 1)}")
    elif 18 <= mass_ind <= 25:
        print("normaal")
        print(f"Идеальный вес: {round(mass_id, 1)}")
        print(f"Индекс массы тела: {round(mass_ind, 1)}")
        print(f"Процент жира: {round(zhir_protsent, 1)}")
    elif 25 < mass_ind <= 30:
        print("ulekaal")
        print(f"Идеальный вес: {round(mass_id, 1)}")
        print(f"Индекс массы тела: {round(mass_ind, 1)}")
        print(f"Процент жира: {round(zhir_protsent, 1)}")
    elif mass_ind > 30:
        print("ei voi olla!")

else:
    print("Неправильно ввели данные")





