dollars = 80.19
euro = 91.44

print('Конвертер валют')
print('''1. RUB -> USD
2. USD -> RUB
3. RUB -> EUR
4. EUR -> RUB
5. Выход''')

while True:
    a = input("Ваш выбор: ")
    while a not in ('1', '2', '3', '4', '5'):
        print("Некорректный выбор")
        a = input("Ваш выбор: ")
    if a == '1':
        rub = float(input("Введите количество рублей: "))
        print(round(rub / dollars, 2))
    elif a == '2':
        usd = float(input("Введите количество бачей: "))
        print(round(usd * dollars, 2))
    elif a == '3':
        rub = float(input("Введите количество рублей: "))
        print(round(rub / euro, 2))
    elif a == '4':
        eur = float(input("Введите количество евро: "))
        print(round(eur * euro, 2))
    else:
        break