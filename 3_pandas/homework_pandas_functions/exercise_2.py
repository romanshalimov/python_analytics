# Используйте файл keywords.csv.
# Нужно написать гео-классификатор, который каждой строке сможет выставить географическую принадлежность
# определённому региону. Т. е. если поисковый запрос содержит название города региона, то в столбце ‘region’
# пишется название этого региона. Если поисковый запрос не содержит названия города, то ставим ‘undefined’.
# Результат классификации запишите в отдельный столбец region.

import pandas as pd

geo_data = {
'Центр': ['москва', 'тула', 'ярославль'],
'Северо-Запад': ['петербург', 'псков', 'мурманск'],
'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
}

df = pd.read_csv('keywords.csv')

def regions(row):
    for region, cities in geo_data.items():
        for city in cities:
            if city in row['keyword']:
                return region
    return 'undefined'

df['region'] = df.apply(regions, axis=1)

show = df[df['region'] != 'undefined']
print(show[0:10])