from random import randint
with open("random.txt","w") as file:
    for num in range(10):
        file.write(str(randint(0, 10)) + " ")