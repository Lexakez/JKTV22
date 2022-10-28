slovo = input("Загадай слово: ")
popqtki = len(slovo)
run = True
ugadaj = "_" * len(slovo)
print(f"Угадай солово: {'_' * len(slovo)}")

while run:
    print(f"У вас осталось: {popqtki} попыток")
    bukva = input("Введите букву: ")
    slovo = slovo.lower()
    if popqtki == 0:
        run = False
        print("Вы проиграли :C")

    if bukva in slovo:
        itog = ""
        for i in range(len(slovo)):
            if bukva == slovo[i]:
                itog += bukva
            else:
                itog += ugadaj[i]
        ugadaj = itog
    else:
        print(f"Буквы '{bukva}' нет в этом слове")
        popqtki -= 1
    if ugadaj == slovo:
        run = False
        print("Победа")
    print(f"Слово: {ugadaj}")

