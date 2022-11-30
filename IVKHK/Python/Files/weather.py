from random import randint
import webbrowser
with open("weather.txt","w") as file:
    file.write("January: ")
    for i in range(31):
        file.write(str(randint(-20, 0)) + ",")
    file.write("\n")
    file.write("February: ")
    for i in range(28):
        file.write(str(randint(-10, 5)) + ",")
    file.write("\n")
    file.write("March: ")
    for i in range(31):
        file.write(str(randint(-5, 10)) + ",")
    file.write("\n")
    file.write("April: ")
    for i in range(30):
        file.write(str(randint(0, 10)) + ",")
    file.write("\n")
    file.write("May: ")
    for i in range(31):
        file.write(str(randint(5, 15)) + ",")
    file.write("\n")
    file.write("June: ")
    for i in range(30):
        file.write(str(randint(10, 20)) + ",")
    file.write("\n")
    file.write("Jule: ")
    for i in range(31):
        file.write(str(randint(10, 30)) + ",")
    file.write("\n")
    file.write("August: ")
    for i in range(31):
        file.write(str(randint(10, 25)) + ",")
    file.write("\n")
    file.write("September: ")
    for i in range(30):
        file.write(str(randint(10, 20)) + ",")
    file.write("\n")
    file.write("October: ")
    for i in range(31):
        file.write(str(randint(5, 10)) + ",")
    file.write("\n")
    file.write("December: ")
    for i in range(30):
        file.write(str(randint(-10, 0)) + ",")
    file.write("\n")
webbrowser.open("weather.txt") 
temp = []
with open("weather.txt", "r") as file:
    pogoda = file.readlines()
    for i in pogoda:
        temp.append((i[i.find(":") + 2 : -2]).split(","))
    # print(temp)

day = int(input("Введите день: "))
month = int(input("Введите месяц: "))
print(f"Температура в этот день: {temp[month - 1][day - 1]}")

month = int(input("Введите номер месяца: "))
print(f"Максимальная температура за месяц: {max(temp[month - 1])}")

month = int(input("Введите номер месяца: "))
sred = 0
for i in temp[month - 1]:
    sred += int(i)
print(f"Средняя температура в этом месяце: {sred / len(temp[month - 1])}")
sred = 0
for i in temp:
    for j in i:
        sred += int(j)
print(f"Средняя температура за год: {round((sred / 365), 2)}")



        
