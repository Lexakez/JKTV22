from math import *
from turtle import st
'''
Задача 1
'''

# stroka = input("Введите строку: ")
# print(f"1.   {stroka[2]} \n2.   {stroka[-2]}\n3.   {stroka[0: 5]}\n4.   {stroka[0: -2]}\n5.   {stroka[0::2]}\n6.   {stroka[1::2]}\n7.   {stroka[:: -1]}\n8.   {stroka[-1:: -2]}\n9.   {len(stroka)}")

'''
Задача 2
'''

# stroka = input("Введите строку: ")
# print(f"Количество слов : {stroka.count(' ') + 1}")

'''
Задача 3
'''

# stroka = input("Введите строку: ")
# print(stroka[ceil(len(stroka) / 2): ] + stroka[0: ceil(len(stroka) / 2)])

'''
Задача 4
'''

# stroka = input("Введите строку: ")
# print(stroka[stroka.find(" "): ], stroka[0: stroka.find(" ")])

'''
Задач 5
'''

# stroka = input("Введите строку: ")
# if stroka.count("f") == 1:
#     print(stroka.find("f"))
# elif stroka.count("f") > 1:
#     print(stroka.find("f"), stroka.rfind("f"))
# else:
#     print()

'''
Задача 6
'''

# stroka = input("Введите строку: ")
# if stroka.count("f") >= 1:
#     print(stroka.find("f", stroka.find("f") + 1))
# elif stroka.count("f") == 0:
#     print(-2)

'''
Задача 7
'''

# stroka = input("Введите строку: ")
# stroka = stroka[0: stroka.find("h")] + stroka[stroka.rfind("h") + 1: ]
# print(stroka)

'''
Задача 8
'''

# stroka = input("Введите строку: ")
# print(stroka[stroka.rfind("h") - 1: stroka.find("h"): -1])

'''
Задача 9
'''

# stroka = input("Введите строку: ")
# print(stroka.replace("1", "one "))

'''
Задача 10
'''

# stroka = input("Введите строку: ")
# stroka = stroka.replace("@", "")
# print(stroka)

'''
Задача 11
'''

# stroka = input("Введите строку: ")
# print(stroka[0: stroka.find("h") + 1] + stroka[stroka.find("h") + 1: stroka.rfind("h")].replace("h", "H") + stroka[stroka.rfind("h"): ])

'''
Задача 12
'''

# stroka = input("Введите строку: ")
# for bukva in range(len(stroka)):
#     if bukva % 3 == 0:
#         stroka = stroka.replace(stroka[bukva], 'x', 1)
# print(stroka.replace("x", ""))
