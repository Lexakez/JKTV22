euro = int(input("Введите сколько евро стоит один пирожок: "))

cent = int(input("Введите сколько центов стоит один пирожок: "))

pir = int(input("Введите сколько пирожков вы хотите купить: "))

euro *= pir

cent *= pir

summaEu = euro + (cent // 100)

summaCent = cent % 100

print(f"Вам надо {summaEu} евро и {summaCent} центов")