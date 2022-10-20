from random import randint

run = True 

while run:
    user_dice = int(input("Введи сколько очков выпадет(от 2 до 12): "))
    randice_1 = randint(1, 6)
    randice_2 = randint(1, 6)
    if user_dice >= 2 and user_dice <= 12:
        if user_dice == randice_1 + randice_2:
            print(f"Вы победили, выпали кубы {randice_1} и {randice_2}")
        else:
            print(f"Вы проиграли, выпали кубы {randice_1} и {randice_2}")
    elif user_dice == 0:
        print("Вы вышли")
        run = False
    else:
        print("Вы ввели не правильное значение.")