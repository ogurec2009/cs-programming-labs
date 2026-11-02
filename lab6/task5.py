n = int(input())

if n < 1 or n > 10:
    print("Ошибка")
else:
    for i in range(n):
        s = ""
        for j in range(n):
            if i >= j:
                dist = i - j
            else:
                dist = j - i
            if j > 0:
                s += " "
            s += str(dist)
        print(s)
