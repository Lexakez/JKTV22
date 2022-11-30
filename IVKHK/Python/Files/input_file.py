user = input("Enter something: ")

with open("something.txt","w") as file:
    file.write(user)