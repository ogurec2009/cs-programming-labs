ticket_cost = float(input())
age = int(input())

if ticket_cost <= 0 and ( 120 >= age >= 0):
    print("Ошибка")

if age <= 5:
    coeffed_ticket_cost = 0
elif 17 >= age >= 6:
    coeffed_ticket_cost = ticket_cost * 0.5
elif 18 >= age >= 59:
    coeffed_ticket_cost = ticket_cost
else:
    coeffed_ticket_cost = ticket_cost * 0.7


print(f"Стоимость: {coeffed_ticket_cost:.2f} руб")
