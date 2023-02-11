# Задание 1. Скачайте с сайта https://grouplens.org/datasets/movielens/ датасет любого размера.
# Определите какому фильму было выставлено больше всего оценок 5.0.

# import urllib.request
import zipfile as generation_z
import pandas as pd

# импортируем файл с сайта
# destination = 'ml-10m.zip'
# url = 'https://files.grouplens.org/datasets/movielens/ml-10m.zip'
# urllib.request.urlretrieve(url, destination)

zip_package = 'ml-10m.zip'

# укажем пути к файлам
movies_in_zip = zip_package.strip('ml-10m.zip') + 'ml-10M100K/movies.dat'                                                                          
ratings_in_zip = zip_package.strip('ml-10m.zip') + 'ml-10M100K/ratings.dat'

# создадим объект с данными
with generation_z.ZipFile(zip_package, 'r') as data_in:
    # data_in.printdir()
    # print(data_in.namelist())
    
    # декодируем файлы в текстовый формат
    with data_in.open(movies_in_zip, 'r') as m:
        movies_list = [bytes.decode(line_, 'ISO-8859-1') for line_ in m.readlines()]
    
    # сохраним файлы в директории
    with open('movies_list.txt', 'w', encoding='utf-8') as out_file_1:
        out_file_1.writelines(''.join(movies_list))

    with data_in.open(ratings_in_zip, 'r') as r:
        ratings_list = [bytes.decode(line_, 'ISO-8859-1') for line_ in r.readlines()]
  
    with open('ratings_list.txt', 'w', encoding='utf-8') as out_file_2:
        out_file_2.writelines(''.join(ratings_list))
    
# создадим датафреймы
with open('movies_list.txt', 'r', encoding='utf-8') as file_m:
    dfm = pd.read_csv(file_m, sep=r'::', names = ['MovieID', 'Title', 'Genres'], engine='python')
    
with open('ratings_list.txt', 'r', encoding='utf-8') as file_r:
    dfr = pd.read_csv(file_r, sep=r'::', names = ['UserID', 'MovieID', 'Rating', 'Timestamp'], engine='python')

# print(dfm.head(10))
# print(dfr.head(10))

joined = dfr.merge(dfm, on='MovieID', how='left')
fltr_cls = joined[['Title', 'Rating']]
filtered = fltr_cls.query('Rating == 5')

result = filtered['Title'].value_counts().head(1)
print(str(result).split('  ')[0])

