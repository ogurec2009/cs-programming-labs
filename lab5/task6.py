n = int(input())

odds = 0

for i in range(n):
    for j in range(i+1):
        c = 1
        for d in range(1, j+1):
            c = c * (i - d + 1) // d
        if c % 2 != 0:
            odds += 1
        print(c, end="")
        if j != i:
            print(end=" ")

    print()

print(f"Нечетных элементов: {odds}")
