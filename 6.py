n = int(input())

length = 1
count = 9
start = 1

while n > length * count:
    n = n - length * count
    length = length + 1
    count = count * 10
    start = start * 10

index = (n - 1) // length
number = start + index

digit_index = (n - 1) % length
digit = int(str(number)[digit_index])

print(digit)
