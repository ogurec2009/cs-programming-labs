numbers = input().split()
finding = input()
indexes = []

for i, n in enumerate(numbers):
    if n == finding:
        indexes.append(i)

print(f"Индексы: {indexes}")
