number_1 = int(input("Введите первое целое число: "))
number_2 = int(input("Введите второе целое число: "))
number_3 = int(input("Введите третье целое число: "))

if number_1 > number_2 and number_1 > number_3:
    print(number_1)
elif number_2 > number_3 and number_2 > number_1:
    print(number_2)
elif number_3 > number_1 and number_3 > number_2:
    print(number_3)
else:
    print("Все числа равны")