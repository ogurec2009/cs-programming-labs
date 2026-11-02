n = int(input())

if n < 0:
    print("Ошибка")
elif n == 0:
    print("Цифр: 1\nСумма цифр: 0")
else:
    sum_of_digits = 0
    amount_of_digits = 0
    while n:
        sum_of_digits += n % 10
        amount_of_digits += 1
        n //= 10
    print(f"Цифр: {amount_of_digits}\nСумма цифр: {sum_of_digits}")
