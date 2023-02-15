# Используйте файл с оценками фильмов ml-latest-small/ratings.csv. Посчитайте среднее время жизни пользователей,
# которые выставили более 100 оценок. Под временем жизни понимается разница между максимальным
# и минимальным значениями столбца timestamp для данного значения userId.

import pandas as pd

df = pd.read_csv('ratings.csv')

ratings = pd.read_csv('ratings.csv')

ratings_max = ratings.groupby('userId').max().reset_index()
ratings_min = ratings.groupby('userId').min().reset_index()
ratings_pt = ratings.pivot_table(index = 'userId', 
                                 columns = 'rating', 
                                 values = 'timestamp', 
                                 margins = 'true', 
                                 aggfunc = 'count'
                                )
filteredratings = ratings_pt.query('All > 100').reset_index()
filtered_rat_max = filteredratings.join(ratings_max['timestamp'], 
                                        on = 'userId', how = 'left').rename(columns = {'timestamp':'Timestamp_max'})
filtered_rat_min_max = filtered_rat_max.join(ratings_min['timestamp'], 
                                             on = 'userId', how = 'left').rename(columns = {'timestamp':'Timestamp_min'})
filtered_rat_min_max['time_of_life'] = filtered_rat_min_max['Timestamp_max'] - filtered_rat_min_max['Timestamp_min']
filtered_rat_min_max[['userId','time_of_life']].time_of_life.mean()