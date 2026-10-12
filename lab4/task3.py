x = float(input())
y = float(input())

if not x and not y:
    print("Начало координат")
elif x and not y:
    print("Ось X")
elif not x and y:
    print("Ось Y")
elif x > 0 and y > 0:
    print("I четверть")
elif x < 0 and y > 0:
    print("II четверть")
elif x < 0 and y < 0:
    print("III четверть")
else:
    print("IV четверть")
