n = int(input())
d = 0
i = 2

while i*i <= n:
    if n % i == 0:
        d = i
        break
    i += 1

if d or n <= 1:
    print("Не простое")
else:
    print("Простое")
