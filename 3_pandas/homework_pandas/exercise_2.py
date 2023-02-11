# Задание 2
# По данным файла power.csv посчитайте суммарное потребление стран Прибалтики (Латвия, Литва и Эстония)
# категорий 4, 12 и 21 за период с 2005 по 2010 год. Не учитывайте в расчётах отрицательные значения quantity.

import pandas as pd

power = pd.read_csv('power.csv')
power.head(10)

baltic_states = power[
    (power['country'] == 'Latvia') | 
    (power['country'] == 'Lithuania') | 
    (power['country'] == 'Estonia')]
baltic_category = baltic_states[(baltic_states.category == 4) |
              (baltic_states.category == 12)|
              (baltic_states.category == 21)
             ]               
baltic_years = baltic_category[(baltic_category.year >= 2005)&
                           baltic_category.year <= 2010
             ]       
baltic_quantities = baltic_years[baltic_years.quantity > 0.0]
total_consumption = baltic_quantities.quantity.sum()
print(f'Суммарное потребление стран Прибалтики за период с 2005 по 2010 = {total_consumption} единиц') 