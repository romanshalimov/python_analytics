# Имеется матрица покупок в интернет-магазине. Столбец А - ID пользователя. Остальные столбцы - количество покупок категорий товаров этим пользователем
# Матрица в виде numpy array

# На сайт заходит очередной посетитель, о покупках которого известно следующее:
# next_user_stats = np.array([0, 1, 2, 0, 0, 0])
    
# Найдите индекс самого похожего пользователя max_index, т.е. посчитайте косинусное сходство между этим пользователем и всеми пользователями из массива user_stats.
# Нумерацию индексов следует начинать с 0   
    
import numpy as np

users_stats = np.array(
    [
        [2, 1, 0, 0, 0, 0],
        [1, 1, 2, 1, 0, 0],
        [2, 0, 1, 0, 0, 0],
        [1, 1, 2, 1, 0, 1],
        [0, 0, 1, 2, 0, 0],
        [0, 0, 0, 0, 0, 5],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 3],
        [1, 0, 0, 2, 1, 4]
    ], 
)

next_user_stats = np.array([0, 1, 2, 0, 0, 0])

next_user_length = np.linalg.norm(next_user_stats)
cosine_convergence = []

for user in users_stats:
    old_user_length = np.linalg.norm(user)
    cosinus = np.dot(next_user_stats,user) / (next_user_length*old_user_length)
    cosine_convergence.append(cosinus)

print(cosine_convergence.index(max(cosine_convergence)))
    
    
    
    
    
    
    
    
    