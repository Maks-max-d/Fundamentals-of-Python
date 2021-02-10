import sys

argv = sys.argv[1:]
zp_flag = 1

try:
    zp = float(argv[0]) * float(argv[1]) + float(argv[2])
except TypeError:
    zp_flag = 0
except ValueError:
    zp_flag = 0
except IndexError:
    zp_flag = 0

if zp_flag == 1 and len(argv) == 3:
    print(f'Выработка в часах = {argv[0]}\n'
          f'Ставка в час = {argv[1]}\n'
          f'Премия = {argv[2]}\n'
          f'Заработная плата = {zp}')
else:
    print('Некорректные данные!')
