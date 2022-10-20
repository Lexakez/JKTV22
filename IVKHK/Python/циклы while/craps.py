from random import randint

run = True

while run:
    shoot = input("Нажми энтер чтоб бросить коcти: ")
    randice_1 = randint(1, 6)
    randice_2 = randint(1, 6)
    if shoot == shoot:
        if randice_1 + randice_2 == 7 or randice_1 + randice_2 == 11:
            print(f"Вы победили у вас выпали кубики {randice_1} и {randice_2}")
            run = False
        elif randice_1 + randice_2 == 2 or randice_1 + randice_2 == 3 or randice_1 + randice_2 == 12:
            print(f"Вы проиграли у вас выпали кубики {randice_1} и {randice_2}")
            run = False
        else:
            user_dice = randice_1 + randice_2
            print(f"У вас выпали кубики {randice_1} и {randice_2} вам надо опять выкинуть {user_dice} очков чтоб победить.")
            shoot = input("Нажми энтер чтоб бросить коcти: ")
            if shoot == shoot:
                randice_1 = randint(1, 6)
                randice_2 = randint(1, 6)
                if randice_1 + randice_2 == user_dice:
                    print(f"Вы победили у вас выпали кубики {randice_1} и {randice_2}")
                    run = False
                elif randice_1 + randice_2 == 7:
                    print(f"Вы проиграли, у вас выпало {randice_1 + randice} очков")
                    run = False 
                else:
                    print(f"Вы проиграли у вас выпали кубики {randice_1} и {randice_2}")
                    run = False

        