from random import *
from time import sleep

win = False

run = True

ruka = []

krup = []

koloda_1 = ["2 Пики", "3 Пики", "4 Пики", "5 Пики", "6 Пики", "7 Пики", "8 Пики", "9 Пики", "10 Пики", "J Пики", "Q Пики", "K Пики", "A Пики",
          "2 Буби", "3 Буби", "4 Буби", "5 Буби", "6 Буби", "7 Буби", "8 Буби", "9 Буби", "10 Буби", "J Буби", "Q Буби", "K Буби", "A Буби",
          "2 Крести", "3 Крести", "4 Крести", "5 Крести", "6 Крести", "7 Крести", "8 Крести", "9 Крести", "10 Крести", "J Крести", "Q Крести", "K Крести", "A Крести",
          "2 Черви", "3 Черви", "4 Черви", "5 Черви", "6 Черви", "7 Черви", "8 Черви", "9 Черви", "10 Черви", "J Черви", "Q Черви", "K Черви", "A Черви"]
balance = 1000

def summa_krup(krup: list) -> int:
    tuz = 0
    krup_sum = 0

    for karta in krup:
        if karta[0].isdigit() and karta[1] == "0":
            krup_sum += int(karta[0] + karta[1])
        elif karta[0].isdigit():
            krup_sum += int(karta[0])
        elif karta[0] == "Q" or karta[0] == "J" or karta[0] == "K":
            krup_sum += 10
        elif karta[0] == "A":
            tuz += 1
            if tuz == 2 and len(ruka) == 2:
                print("Победа")
            krup_sum += 11
        if krup_sum > 21 and tuz >= 1:
            krup_sum -= 10
    tuz = 0
    return krup_sum


def summa_kart (ruka: list) -> int:
    #Подсчет карт в руке игрока
    tuz = 0
    kart_sum = 0

    for karta in ruka:
        if karta[0].isdigit() and karta[1] == "0":
            kart_sum += int(karta[0] + karta[1])
        elif karta[0].isdigit():
            kart_sum += int(karta[0])
        elif karta[0] == "Q" or karta[0] == "J" or karta[0] == "K":
            kart_sum += 10
        elif karta[0] == "A":
            tuz += 1
            if tuz == 2 and len(ruka) == 2:
                kart_sum = 21
                continue
            kart_sum += 11
        if kart_sum > 21 and tuz >= 1:
            kart_sum -= 10
    tuz = 0
    return kart_sum

while run:
    if balance > 0:
        koloda = koloda_1
        shuffle(koloda)
        print(f"У вас на счету: {balance}$")
        stavka = abs(int(input("Введите ставку: ")))
        if stavka > balance:
            print("===Не хватает баланса===")
        else:
            balance -= stavka

# Раздача карт игроку

            ruka.append(koloda[-1])
            koloda.pop(-1)
            ruka.append(koloda[-1])
            koloda.pop(-1)
            ruka_txt = ruka[0] +" и "+ ruka[1]
            print(f"У вас на руках карты {ruka_txt}")

            tuz = 0
            kart_sum = 0

# Подсчет карт игрока

            kart_sum = summa_kart(ruka)
            print(kart_sum)
            print(f"Сумма ваших карт: {kart_sum}")
            if kart_sum == 21:
                print("---===Победа===---")
                win = True
                balance += stavka * 2.5
                continue


# Раздача карт крупье

            krup.append(koloda[-1])
            koloda.pop(-1)
            krup.append(koloda[-1])
            koloda.pop(-1)
            krup_txt = krup[0] + " и " + krup[1]
            print(f"У крупье карты: {krup[0]} и *******")

# Решение игрока брать не брать карты

            nabor = True
            while nabor:
                choice = input("Хотите взять еще карту?(Да/нет, +/-): ")
                if choice.lower() == "да" or choice == "+":
                    print("-" * 10)
                    ruka.append(koloda[-1])
                    koloda.pop(-1)
                    ruka_txt += " и " + ruka[-1]
                    print(f"У вас на руках: {ruka_txt}")
                    kart_sum = summa_kart(ruka)
                    print(f"Сумма ваших карт: {kart_sum} ")
                    if kart_sum == 21:
                        print("---===Победа===---")
                        balance += stavka * 2
                        win = True
                    if kart_sum > 21:
                        print("---===Вы проиграли===---")
                        nabor = False
                        win = True
                else:
                    nabor = False

# Набор карт крупье

            nab_krup = True
            while nab_krup:
                krup_sum = summa_krup(krup)
                print("-" * 10)
                print(f"У крупье карты: {krup_txt}")
                print(f"Сумма карт крупье: {krup_sum}")
                sleep(1)
                if krup_sum == 21:
                    print("---===Вы проиграли===---")
                    win = True
                    nab_krup = False
                elif krup_sum <= 16:
                    krup.append(koloda[-1])
                    krup_txt += " и " + koloda[-1]
                    koloda.pop(-1)
                elif krup_sum >= 17:
                    nab_krup = False

# Сравнение карт крупье и игрока

            if win == True:
                continue
            else:
                if krup_sum > kart_sum:
                    print("---===Вы проиграли===---")
                elif krup_sum == kart_sum:
                    print("---===Ничья===---")
                    balance += stavka
                else:
                    print("---===Победа===---")
                    balance += stavka * 2
            koloda = koloda_1
            krup_sum = 0
            kart_sum = 0
            ruka.clear()
            krup.clear()
    else:
        print("Деньги кончились.")
        run = False