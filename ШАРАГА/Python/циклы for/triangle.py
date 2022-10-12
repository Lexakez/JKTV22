number_1 = int(input("enter the num: "))
dot = "*"
space = ""

print("-----1-----")

number = number_1
for num in range(number):
    dot_1 = " *"
    print(dot)
    dot += dot_1

print("-----2-----")

number = number_1
for num in range(number):
    dot_1 = "* "
    dot_1 = dot_1 * number

    print(space, dot_1)
    number -= 1
    space += "  "


print("-----3-----")

number = number_1
for num in range(number):
    dot_1 = "* "
    print(dot_1 * number)
    number -= 1

print("-----4-----")

number = number_1
space_1 = "  "
dot_1 = "* "
for num in range(number):
    print(space_1 * number, dot_1)
    dot_1 += "* "
    number -= 1
