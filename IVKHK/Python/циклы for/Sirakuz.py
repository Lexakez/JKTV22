user_num = int(input("Введите число: "))
eter = 0
while user_num != 1:
    if user_num % 2 == 0:
        user_num /= 2
        print(int(user_num))
    elif user_num % 2 == 1:
        user_num *= 3
        print(int(user_num))
        user_num += 1
        print(int(user_num))
        user_num /= 2
        print(int(user_num))
    eter += 1
print(f"Кол-во итераций: {eter}")