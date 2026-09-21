distance = float(input())
consumption = float(input())
price_of_liter = float(input())

gas = consumption * distance / 100
full_price = gas * price_of_liter

print(f"Топливо: {gas:.2f} л")
print(f"Стоимость: {full_price:.2f} руб")
