with open("users.txt", "w") as file:
    n = int(input("Количество людей:"))
    for i in range(n):
        file.write(input("Name:") + ", " + input("ID:"))