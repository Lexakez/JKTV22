from random import randint

'''
Задача №1
'''

# n = int(input("Введите ограниечение: "))
# num = 1
# while num ** 2 < n:
#     print(f"{num} ** 2 = {num ** 2}")
#     num += 1

'''
Задача №2
'''

# num = int(input("Введите целое число не меньше двух: "))
# delitel = 2 
# while num % delitel != 0:
#     delitel += 1
# print(delitel)

'''
Задача №3
'''

# num = int(input(":"))
# stepen = 2
# chislo_stepeni = 1
# while stepen <= num:
#     stepen *= 2
#     chislo_stepeni += 1
# print(f"2 ** {chislo_stepeni - 1}, = {stepen // 2}")

'''
Задача №4
'''

# km = int(input("Введите количество км за первый день: "))
# km_vcelom = int(input("Введите пробег спортсмена за все дни: "))
# den = 1
# while km < km_vcelom:
#     km *= 1.1
#     den += 1
# print(f"Он пробежит {km_vcelom} километров на: {den} дней")

'''
Задача №5
'''

# vklad = int(input("Введите сумму вклада: "))
# protsent = int(input("Введите процент вклада: "))
# summa = int(input("Введите конечную сумму: "))
# year = 0
# while vklad < summa:
#     vklad += vklad * protsent / 100
#     year += 1
# print(f"Вам надо ждать {year} лет/год(а)")

'''
Задача №6
'''

# chislo = 0
# number = 1
# while number != 0:
#     number = randint(0, 100)
#     print(number)
#     chislo += 1
# print(f"Кол-во чисел в последовательности: {chislo - 1}")

'''
Задача №7 
'''

# chislo = 0
# number = 1
# while number != 0:
#     number = randint(0, 100)
#     print(number)
#     chislo += number
# print(f"Сумма последовательности: {chislo}")

'''
Задача №8
'''

# chislo = 0
# number = 1
# srednie = 0
# naibolshee = 0
# while number != 0:
#     number = randint(0, 100)
#     print(number)
#     srednie += number
#     chislo += 1
#     if number > naibolshee:
#         naibolshee = number
# print(f"Наибольшее число последовательности: {naibolshee}")
# print(f"Средние значение последовательности: {round((srednie / chislo), 0)}")

'''
Задача №9
'''

# chislo = 0
# number = 1
# index = 0
# amount = 0
# while number != 0:
#     number = randint(0, 100)
#     print(number)
#     amount += 1
#     if number > chislo:
#         chislo = number
#         index = amount
# print(f"Наибольшее число: {chislo} его индекc: {index}")

'''
Задача №10
'''

chislo = 0
number = 1
naibolshee = 0
while number != 0 and chislo < 20:
    number = randint(0, 100)
    print(number)
    chislo += 1
    if naibolshee < number:
        naibolshee = number
print(f"Наибольшее число: {naibolshee} \nКол-во чисел: {chislo}")