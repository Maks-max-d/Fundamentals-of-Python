proceeds = input('Введите выручку организации: ')
costs = input('Введите издержки организации: ')
proceeds = float(proceeds)
costs = float(costs)
if proceeds > costs:
    fin_res = 'Организация прибыльна.'
    print(fin_res)
    profitability = round((proceeds - costs) / proceeds, 2)
    print(f'Рентабельность выручки составляет: {profitability}')
    staff = input('Введите количество сотрудников в организации: ')
    staff = int(staff)
    staff_profit = round((proceeds - costs) / staff, 2)
    print(f'Прибыль в расчете на одного сотрудника составляет: {staff_profit}')
elif proceeds < costs:
    fin_res = 'Организация убыточна.'
    print(fin_res)
else:
    fin_res = 'У организации нет прибыли, нет убытков.'
    print(fin_res)
