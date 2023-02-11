# Задание 2
# По данным файла power.csv посчитайте суммарное потребление стран Прибалтики (Латвия, Литва и Эстония)
# категорий 4, 12 и 21 за период с 2005 по 2010 год. Не учитывайте в расчётах отрицательные значения quantity.

import pandas as pd

power = pd.read_csv('power.csv')
power_1 = power[
    (power['country'].isin(['Latvia', 'Lithuania', 'Estonia']))
    & (power['category'].isin([4, 12, 21]))
    & (power['year'].isin(range(2005, 2011)))
    & (power['quantity'] > 0)
    ]['quantity'] \
    .sum()

print(power_1)