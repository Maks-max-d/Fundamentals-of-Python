s = input('Введите время в секундах: ')
hour = int(s) // 3600
min = (int(s) % 3600) // 60
sec = (int(s) % 3600) % 60
if(hour < 10):
    hour = '0' + str(hour)
if(min < 10):
    min = '0' + str(min)
if(sec < 10):
    sec = '0' + str(sec)
print(f'{hour}:{min}:{sec}')
