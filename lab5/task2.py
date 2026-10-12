a = int(input())
b = int(input())

sum_of_all = 0
multiplication_of_all = 1

for i in range(a, b+1):
    sum_of_all += i
    multiplication_of_all *= i

print(f"Сумма: {sum_of_all}")
print(f"Произведение: {multiplication_of_all}")
