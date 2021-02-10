def fact(n):
    k = 1
    for i in range(1, n + 1):
        k *= i
        yield k

g = fact(8)
for el in g:
    print(el)
