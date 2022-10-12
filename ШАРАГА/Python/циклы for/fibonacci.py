number = int(input("Enter the num: "))
fib_1 = 1
fib_2 = 1

for num in range(number):
    print(f"{fib_1} + {fib_2} = {fib_1 + fib_2}")
    fib_2 = fib_2 + fib_1
    fib_1 = fib_2 - fib_1
    