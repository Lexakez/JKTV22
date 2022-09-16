from math import floor

# Первый вариант

number = float(input("Введите положительное действительное число: "))

number = number - floor(number)

#number = round(number, 2)

print(number)

# Второй вариант

print(number % 1)