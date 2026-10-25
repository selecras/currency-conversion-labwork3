import requests
import os


# очистка консоли
def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


# проверка ввода валют
def try_except(text: str) -> float | None:
    while True:
        try:
            a = float(input(text))
        except Exception as e:
            print("Некорректный ввод")
            continue
        return a


url = "https://www.cbr-xml-daily.ru/daily_json.js"
# пробуем достучаться до url и получить курсы доллара и евро
try:
    response = requests.get(url)
    data = response.json()

    USD = data['Valute']["USD"]['Value']
    EUR = data['Valute']["EUR"]['Value']
# если не получилось -- выходим
except Exception as e:
    print(f"Ошибка при получении данных: {e}")
    exit()

# краткий туториал
clear()
print('''Конвертер валют
1. RUB -> USD
2. RUB -> EUR
3. USD -> RUB
4. EUR -> RUB 
5. Выход
''')
while True:
    choice = input("Ваш выбор: ")
    while choice not in ('1','2','3','4','5'):
        print("Некорректный выбор")
        choice = input("Ваш выбор: ")
    clear()

    # из рублей в доллары или евро
    if choice in ('1', '2'):
        rub = try_except("Введите количество рублей: ")
        res = round(rub / (USD, EUR)[int(choice) - 1], 2)
        print(f"{rub}₽ = {res}{"$€"[int(choice) - 1]}")
    # из доллары в рубли
    elif choice == '3':
        usd = try_except("Введите количество долларов: ")
        res = round(usd * USD, 2)
        print(f"{usd}$ = {res}₽")
    # из евро в рубли
    elif choice == '4':
        eur = try_except("Введите количество евро: ")
        res = round(eur * EUR, 2)
        print(f"{eur}€ = {res}₽")
    # на выход
    else:
        break
    # повторно выводим инструкцию т.к. консоль чистая
    print('''1. RUB -> USD
2. RUB -> EUR
3. USD -> RUB
4. EUR -> RUB 
5. Выход
''')