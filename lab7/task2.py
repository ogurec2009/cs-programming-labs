numbers = list(map(int, input().split()))
squares = []

for n in numbers:
    if n > 0 and n % 2:
        squares.append(n*n)

print(f"Квадраты: {squares}")
