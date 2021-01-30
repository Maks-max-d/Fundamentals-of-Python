n = input('Введите целое положительное число: ')
n = int(n)
k = 0
while n > 0:
    m = int(n) % 10
    n = int(n) // 10
    if m > k:
        k = m
print(k)
