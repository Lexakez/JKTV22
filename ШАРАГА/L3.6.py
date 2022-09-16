number = int(input("Введите трехзначное число: "))

z = number // 100

x = (number % 100) // 10

c = number % 10

print(f"{z} + {x} + {c} = {z + x + c}")

