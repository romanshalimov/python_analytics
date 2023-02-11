# Создайте диагональную матрицу с элементами от N до 0 (N должно входить в массив).
# Посчитайте сумму ее значений на диагонали.
# Впишите свое решение вместо ***
# ВАЖНО: в качестве ответа тренажёр принимает целое число (int).

import numpy as np
 
def sum_matrix(N):
    my_matrix = np.diag(np.flip(np.arange(N,0,-1)))
    return np.trace(my_matrix)
 
print(sum_matrix(5))
print(sum_matrix(10))
print(sum_matrix(15))