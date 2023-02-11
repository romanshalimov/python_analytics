# Задание 1 Напишите функцию, которая классифицирует фильмы из материалов занятия по следующим правилам:
# оценка 2 и меньше - низкий рейтинг
# оценка 4 и меньше - средний рейтинг
# оценка 4.5 и 5 - высокий рейтинг

import pandas as pd

ratings = pd.read_csv('ratings.csv',usecols=['movieId', 'rating'])

def rating_class(rate):
    if rate <= 2.0:
        return "Low Rating"
    elif rate <= 4.0:
        return "Average Rating"
    elif 4.5 <= rate <= 5.0:
        return "High Rating"
    
ratings['class'] = ratings['rating'].apply(rating_class)
ratings.head()
