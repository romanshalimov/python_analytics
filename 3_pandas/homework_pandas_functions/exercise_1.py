# Напишите функцию, которая классифицирует фильмы из материалов занятия по следующим правилам:
# оценка 2 и меньше - низкий рейтинг
# оценка 4 и меньше - средний рейтинг
# оценка 4.5 и 5 - высокий рейтинг

import pandas as pd

# откроем файлы и объединим датафреймы
ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')
df = movies.merge(ratings) # on = 'movieId', inner, outer, left, right

# сгруппируем по названиям фильмов и получим объект датафрейма с уникальными названиями
df_groupby_object = df.groupby(['title'])
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001F6DE06B100>

# вычислим среднее значение рейтинга для каждого фильма и вернём датафрейм
films_classification = df_groupby_object.rating.mean().reset_index()

# функция с условной конструкцией для столбца rating
def rating_classification(row):
    if row['rating'] <= 2:
        return 'Low'
    elif row['rating'] <= 4:
        return 'Average'
    else:
        return 'High'

# применим функцию к столбцам ось 1
films_classification['class'] = films_classification.apply(rating_classification, axis = 1)

films_classification.head
print(films_classification[1234:1239])
