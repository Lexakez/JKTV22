slovo = input("Введите слово: ")
glasnqe = "аеёийоуыэюя"
soglasnqe = "бвгджзклмнпрстфхцчшщ"
glas = 0 
soglas = 0
for bukva in slovo:
    if bukva.lower() in glasnqe:
        glas += 1
    if bukva.lower() in soglasnqe:
        soglas += 1

if glas > soglas:
    print("Гласных больше")
elif soglas > glas:
    print("Согласных больше")
else:
    print("Их поровну")