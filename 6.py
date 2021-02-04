goods_list = []

i = 1
while input('Ввести новый товар (y/n)? ').upper() == 'Y':
    name = input('Наименование: ')
    try:
        cost = float(input('Цена: '))
    except ValueError:
        print('Неверно введена цена!')
        break
    try:
        quantity = float(input('Количество: '))
    except ValueError:
        print('Неверно введено количество!')
        break
    unit = input('Единицы измерения: ')
    goods_dict = {'Наименование' : name, 'Цена' : cost, 'Количество' : quantity, 'Единицы измерения' : unit}
    goods_tuple = (i, goods_dict)
    goods_list.append(goods_tuple)
    i += 1

#goods_list = [(1, {'Наименование': 'Принтер', 'Цена': 1500.0, 'Количество': 1.0, 'Единицы измерения': 'шт.'}), (2, {'Наименование': 'Сканер', 'Цена': 1200.0, 'Количество': 2.0, 'Единицы измерения': 'шт.'}), (3, {'Наименование': 'Бумага', 'Цена': 400.0, 'Количество': 8.0, 'Единицы измерения': 'пачка'})]
print(goods_list)

name_list = []
cost_list = []
quantity_list = []
unit_list = []
for ind, el in enumerate(goods_list):
    name_list.append(el[1].get('Наименование'))
    cost_list.append(el[1].get('Цена'))
    quantity_list.append(el[1].get('Количество'))
    unit_list.append(el[1].get('Единицы измерения'))

analytic_dict = {'Наименование' : name_list, 'Цена' : cost_list, 'Количество' : quantity_list, 'Единицы измерения' : unit_list}
print(analytic_dict)
