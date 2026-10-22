amount_of_buys = 0
cost = 0

while True:
    command = input()

    if command == "stop":
        break

    amount_of_buys += 1
    cost += int(command)
    
if amount_of_buys > 0:
    print(f"Покупок: {amount_of_buys}")
    print(f"Общая стоимость: {cost}")
    print(f"Средняя стоимость: { (cost / amount_of_buys):.2f}")
else:
    print("Нет покупок")
