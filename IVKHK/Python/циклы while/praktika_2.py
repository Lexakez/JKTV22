from random import randint
'''
Задача №1
'''

# run = True
# while run:
#     chetnoe = int(input("Введите четное число: "))
#     if chetnoe % 2 == 0:
#         run = False
#     nechetnoe = int(input("Нечетное число: "))
#     if nechetnoe % 2 == 1:
#         run = False
#     polozitelnoe = int(input("Положительное число: "))
#     if polozitelnoe > 0:
#         run = False
#     otricatelnoe = int(input("Отрицательное число: "))
#     if otricatelnoe < 0:
#         run = False

'''
Задача №2
'''

# cikl = 0
# run = True
# summa = 0
# while run:
#     print("===========================================")
#     number = int(input("Введите число : "))
#     cikl += 1
#     summa += number
#     if number == 0:
#         run = False   
#     print(f"Сумма всех чисел: {summa} \nКол-во чисел: {cikl} \nСреднее значение: {int(round((summa / cikl), 0))}")

'''
Задача №3
'''
pinkod = 1121
bankomat = True
popqtka = 3
vqbor = True

while bankomat:
    pin = int(input("Введите пинкод: "))
    balance = randint(0, 9999)
    if pin != pinkod:
        popqtka -= 1
        print(f"Вы ввели не верный пинкод, у вас осталось: {popqtka} попытка/и")
        if popqtka == 0:
            bankomat = False
            print("Вы ввели не верный пинкод")
    if pin == pinkod:
        while vqbor:
            print("==========")       
            print("1. Положить деньги на счет\n2. Снять деньги со счета\n3. Посмотреть остаток счета\n4. Выйти из банкомата")
            choice = int(input("Выбрать действие: "))
            if choice == 1:
                summa = int(input("Введите сколько хотите внести на счёт: "))
                balance += summa
            if choice == 2:
                summa = int(input("Введите сколько хотите снять со счета: "))
                if summa <= balance:
                    balance -= summa
                    print(f"Вы сняли со счета: {summa} $")
                elif summa > balance:
                    print("На счету не хватает денег :( ")
            if choice == 3:
                print(f"На вашем счету: {balance} $")
            if choice == 4:
                vqbor = False
    if vqbor == False:
        bankomat = False
