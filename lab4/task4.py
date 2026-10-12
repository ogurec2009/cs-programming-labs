a = int(input())
b = int(input())
c = int(input())

if (a < 0) or (b < 0) or (c < 0) or (a > b+c) or (b > a+c) or (c > a+b):
    print("Треугольник не существует")
else:
    if a == b and a == c:
        print("Равносторонний")
    elif (a == b) ^ (a == c) ^ (b == c):
        print("Равнобедренный")
    else:
        print("Разносторонний")
