current_temp = float(input())
wanted_temp = float(input())

if current_temp > wanted_temp:
    print("Охлаждение")
elif current_temp < wanted_temp:
    print("Нагрев")
else:
    print("Выключен")
