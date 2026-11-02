r, c = map(int, input().split())

table = []

for _ in range(r):
    table.append(list(map(int, input().split())))

row_start, row_end, column_start, column_end = map(int, input().split())
finding = int(input())
have_found = False

for i in range(row_start, row_end + 1):
    for j in range(column_start, column_end + 1):
        if table[i][j] == finding:
            have_found = True
            print(f"{i} {j}")

if not have_found:
    print("Не найдено")
