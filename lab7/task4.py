r, c = map(int, input().split())

table = []

for _ in range(r):
    table.append(list(map(int, input().split())))

sum_of_rows = []
sum_of_columns = []

for i in range(r):
    row_sum = 0
    for j in range(c):
        row_sum += table[i][j]
    sum_of_rows.append(row_sum)

for j in range(c):
    columns_sum = 0
    for i in range(r):
        columns_sum += table[i][j]
    sum_of_columns.append(columns_sum)

print(f"Суммы строк: {sum_of_rows}")
print(f"Суммы столбцов: {sum_of_columns}")
