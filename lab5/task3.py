n = int(input())

below_zeroes = 0
zeroes = 0
above_zeroes = 0

while n:
    i = float(input())
    if i < 0:
        below_zeroes += 1
    elif i > 0:
        above_zeroes += 1
    else:
        zeroes += 1
    n -= 1

print(f"Ниже нуля: {below_zeroes}")
print(f"Равны нулю: {zeroes}")
print(f"Выше нуля: {above_zeroes}")
