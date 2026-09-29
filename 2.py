number = int(input())

if number % 2 == 0:
    print("Четное")
else:
    print("Нечетное")

if number > 0:
    print("Положительное")
elif number < 0:
    print("Отрицательное")
else:
    print("Ноль")

if 10 <= number <= 50:
    print("Принадлежит отрезку [10,50]")
else:
    print("Не принадлежит отрезку [10,50]")
