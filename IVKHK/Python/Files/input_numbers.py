with open("numbers.txt", "w") as file:
    for i in range(5):
        file.write(input("Введите число:") + "\n")
