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

num = int(input(":"))
stepen = 2
chislo_stepeni = 1
while stepen <= num:
    stepen *= 2
    chislo_stepeni += 1
    print(f"2 ** {chislo_stepeni - 1}, = {stepen // 2}")

'''
Задача №4
'''

# km = int(input("Введите количество км за первый день: "))
# km_vcelom = int(input("Введите пробег спортсмена за все дни: "))
# den = 0
# while km + km * 0.1 < km_vcelom:
#     den += 1
#     print(den)
