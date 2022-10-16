number_1 = int(input("Enter the numnber: "))
dot = "* "
space = " "
number = number_1
dot_count = 1
for dots in range(number):
    print(space, dot * number)
    number -= 1
    space += " "
    if number == 0:
        number = number_1
        space = " "
        for dots in range(number):
            print(space * number, dot * dot_count)
            number -= 1
            dot_count += 1