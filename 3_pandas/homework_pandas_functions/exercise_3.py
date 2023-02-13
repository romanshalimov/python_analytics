import pandas as pd

ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')
df = ratings.merge(movies, on = 'movieId')
# movies.merge(ratings)

# переменная years c числовым списком
years = list(range(1950, 2011))

# функция для названия фильма
def production_year(title):
    for year in years:
        if str(year) in title:
            return year
    return 1900

df['year'] = df['title'].apply(production_year)

ratings_years = df[['rating', 'year']].groupby(by = 'year').mean().sort_values('rating', ascending=False)
ratings_years.head
