#Дан поток дат в формате YYYY-MM-DD, в которых встречаются некорректные значения:
#stream = [‘2018-04-02’, ‘2018-02-29’, ‘2018-19-02’]
#Напишите функцию, которая проверяет эти даты на корректность. То есть для каждой даты
#возвращает True — дата корректна или False — некорректная.

from datetime import datetime

stream = ['2018-04-02', '2018-02-29', '2018-19-02']

def check(list_of_dates):
    for days in list_of_dates:
        try:
            datetime.strptime(days, '%Y-%m-%d')
            print(f'{days} - True')
        except:
            print(f'{days} - False')
            
check(stream)