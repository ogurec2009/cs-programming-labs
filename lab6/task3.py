n = int(input())

if n < 2:
    print("Ошибка")
else:
    i = 2
    first = True
    while n > 1:
        if n % i == 0:
            n //= i
            if not first:
                print(" ", end="")

            print(i, end="")
            first = False
        else:
            i += 1
    print()
