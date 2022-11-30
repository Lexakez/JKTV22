myfile = open("hello.txt","w")

myfile.write("Hello world \n")

myfile.close()

with open("hello.txt","a") as file:
    file.write("Python")

with open("hello.txt","r") as file:
    content = file.readlines()

for txt in content:
    print(txt)