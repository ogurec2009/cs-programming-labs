raw = input()

train_id, departure_from, destination_to, takes_off_at, cost = raw.split(";")
cost = float(cost)

print(f"Поезд: {train_id}\nМаршрут: {departure_from} - {destination_to}\nОтправление: {takes_off_at}\nЦена: {cost:.2f} руб")
