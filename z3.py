print("☕ Добро пожаловать в кафе!\n")
print("Меню:")
print("1. Эспрессо       — 120₽")
print("2. Капучино       — 180₽")
print("3. Латте          — 200₽")
print("4. Американо      — 150₽")
print("5. Горячий шоколад — 220₽\n")

ESPRESSO = 120
CAPPUCCINO = 180
LATTE = 200
AMERICANO = 150
CHOCOLATE = 220

drink = input("Введите номер или название напитка: ").strip().lower()

match drink:
    case "1" | "эспрессо":
        name, price = "Эспрессо", ESPRESSO
    case "2" | "капучино":
        name, price = "Капучино", CAPPUCCINO
    case "3" | "латте":
        name, price = "Латте", LATTE
    case "4" | "американо":
        name, price = "Американо", AMERICANO
    case "5" | "горячий шоколад" | "шоколад":
        name, price = "Горячий шоколад", CHOCOLATE
    case _:
        print("\n❗ Ошибка: напиток не найден. Перезапустите программу")

qty = int(input("Введите кол-во порций: "))
def portions_word(n):
    if n % 10 == 1 and n % 100 != 11:
        return "порция"
    elif 2 <= n % 10 <= 4 and not (12 <= n % 100 <= 14):
        return "порции"
    else:
        return "порций"

total = price * qty
discount_code = input("Введите код скидки (SALE10/STUDENT15): ").strip().upper()
discount = 0

match discount_code:
    case "SALE10":
        discount = 0.10
    case "STUDENT15":
        discount = 0.15
    case _:
        discount = 0

final_price = total * (1 - discount)
print("\n" + "═" * 44)
print("               🧾 ЧЕК КАФЕ")
print("═" * 44)
print(f"Напиток:           {name}")
print(f"Цена за порцию:    {price}₽")
print(f"Количество:        {qty} {portions_word(qty)}")
print(f"Сумма:             {total}₽")

if discount > 0:
    print(f"Скидка:            {int(discount * 100)}%")
    print(f"ИТОГО К ОПЛАТЕ:    {final_price:.2f}₽")
else:
    print("Скидка:            нет")
    print(f"ИТОГО К ОПЛАТЕ:    {final_price:.2f}₽")

print("═" * 44)
print("Спc за заказ!что бы был 🤍завтра и купил снова!🤍")
print("═" * 44)