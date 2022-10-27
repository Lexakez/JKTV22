kood = input("Введи ваш личный код: ")
if kood[0] == str(3) or kood[0] == str(5):
    print("Пол: Мужчина")
elif kood[0] == str(4) or kood[0] == str(6):
    print("Пол: Женщина")
print(f"Дата рождения: {kood[5: 7]}.{kood[3: 5]}.{kood[1: 3]}")
if int(kood[7: 10]) in range(220, 270):
    print("Код зарегестрирован в центральной больнице Ида-Вирумаа, Кохтла ярве")
kontroll_num = int(kood[0]) * 1 + int(kood[1]) * 2 + int(kood[2]) * 3 + int(kood[3]) * 4 + int(kood[4]) * 5 + int(kood[5]) * 6 + int(kood[6]) * 7 + int(kood[7]) * 8 + int(kood[8]) * 9 + int(kood[9]) * 1
if kontroll_num % 11 >= 10:
    kontroll_num = int(kood[0]) * 3 + int(kood[1]) * 4 + int(kood[2]) * 5 + int(kood[3]) * 6 + int(kood[4]) * 7 + int(kood[5]) * 8 + int(kood[6]) * 9 + int(kood[7]) * 1 + int(kood[8]) * 2 + int(kood[9]) * 3
    if kontroll_num % 11 == int(kood[-1]):
        print("Контрольный номер верный.")
    elif kontroll_num % 11 >= 10:
        if 0 == int(kood[-1]):
            print("Контрольный номер верный.")
        else:
            print("Контрольный номер не верный.")
    else:
        print("Контрольный номер не верный")
elif kontroll_num % 11 < 10:
    if kontroll_num % 11 == int(kood[-1]):
        print("Контрольный номер верный.")
    else:
        print("Контрольный номер не верный.")