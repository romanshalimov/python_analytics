#Напишите функцию date_range, которая возвращает список дат за период от start_date до end_date.
#Даты должны вводиться в формате YYYY-MM-DD. В случае неверного формата или при start_date > end_date
#должен возвращаться пустой список.

from datetime import datetime
from datetime import timedelta

def date_range(start_date, end_date):
    dates_list = []
    try:
        start_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')
        current_date_dt = start_date_dt
    except:
        print(dates_list)
        return
    if current_date_dt > end_date_dt:
        print(dates_list)
    else:
        while current_date_dt <= end_date_dt:
            dates_list.append(current_date_dt.strftime('%Y-%m-%d'))
            current_date_dt += timedelta(days=1)
        print(dates_list)

date_range('2023-01-20', '2023-01-23')
#date_range('2024-01-20', '2023-01-23')


