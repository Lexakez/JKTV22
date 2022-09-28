from random import randint 

test = True
points = 0 
q = 5

while test == True:
    n1 = randint(0, 9)
    n2 = randint(0, 9)
    print(f"Сосчитай {n1} * {n2} = ?")
    answer = int(input("Введи ответ: "))
    if answer == n1 * n2:
        print("Правильно")
        points += 1
        q -= 1
    else:
        print("Не правильно")
        q -= 1
    if q == 0:
        test = False
if points == 5:
    print(f"Отлично у тебя {points} правильных ответов.")
elif points == 4 or points == 3:
    print(f"Не плохо, но можно лучше, у тебя {points} правильных ответов.")
else:
    print(f"Плохо, иди учись, у тебя {points} правильных ответов.")

