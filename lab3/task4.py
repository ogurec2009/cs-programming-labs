raw = input()

train_id, departure_from, destination_to, takes_off_at, cost = raw.split(";")
cost = float(cost)

print(f"Поезд: {train_id}")
print(f"Маршрут: {departure_from} - {destination_to}")
print(f"Отправление: {takes_off_at}")
print(f"Цена: {cost:.2f} руб")
