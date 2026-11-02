remaining_goods = list(map(int, input().split()))

copy = [row for row in remaining_goods]

for i in range(len(copy)):
    if copy[i] < 0:
        copy[i] = 0

print(f"Исходные остатки: {remaining_goods}")
print(f"Исправленные остатки: {copy}")
