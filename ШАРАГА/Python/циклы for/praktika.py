from random import randint

'''
4 Задание
'''

# num2 = 0

# for num in range(10):
#     num = randint(0, 100)
#     num2 += num
#     print(num)
# print(f"сумма всех числе {num2}")

'''
5 Задание
'''

# num2 = 0

# number = int(input("Enter the num: "))
# for num in range(number):
#     num = randint(0, 100)
#     num2 += num
#     print(num)
# print(f"сумма всех числе {num2}")

'''
11 Задание
'''

# n = int(input("Введите количество карт: "))
# karto4ka = 0
# rankart = randint(1, n)
# for kart in range(1, n + 1):
#     if kart == rankart: 
#         karto4ka = kart
#         continue
#     else:
#         print(kart, end = (" "))
# print(f"Потерялась карточка №{karto4ka}")
    

    


'''
10 Задание
'''

# n = int(input("Enter the number: "))
# for num in range(n):
#     for number in range(1, num + 2):
#         print(number, end = '')
#     print()


'''
3 Задание
'''

# a = int(input(":"))
# b = int(input(":"))

# for num in range(a - int((a % 2) == 0), b - 1, -2):
#     print(num)

'''
9 Задание
'''
# n = int(input("Введите количество цифр: "))
# cikl = 0
# nol = 0
# while n != cikl:
#     number = input("Введите целое число: ")
#     cikl += 1
#     if number == "":
#         n = cikl
#     for zero in str(number):
#         if zero == "0":
#             nol += 1
# print(nol)

'''
Задача 11
'''

n = int(input("Введите кол-во карточек: "))
koloda = []
while len(koloda) != n - 1:
    rankart = randint(1, n)
    if rankart not in koloda:
        koloda.append(rankart)
print(koloda)
for kart in range(1, n):
    if kart not in koloda:
        print(kart)