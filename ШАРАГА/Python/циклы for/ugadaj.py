from random import randint

run = True
random_num = randint(0, 10)
tryes = 0

while run:
    number = int(input("Guess the number: "))
    if number == random_num:
        print("Right!!!")
        print(f"Count of your attempts: {tryes}")
        run = False
    elif number > random_num:
        print("Your number bigger than random num")
        tryes += 1
    elif number < random_num:
        print("Your number smaller than random num")
        tryes += 1