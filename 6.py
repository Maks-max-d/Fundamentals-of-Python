from itertools import count, cycle

x = 25
my_list = [2, 5, 3]

for i in count(x, 1):
    print(i)
    if i > 28:
        break

c = 0
for el in cycle(my_list):
    if c > 3:
        break
    print(el)
    c += 1
