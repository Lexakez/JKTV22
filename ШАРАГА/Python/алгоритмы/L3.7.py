from math import *

number = float(input("Введите положительное число: "))

dr = number % 1

if dr < 0.5:
    number = floor(number)
else:
    number = ceil(number)

print(number)