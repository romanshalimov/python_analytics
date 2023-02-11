# Создайте numpy array с элементами от числа N до 0. Например, для N = 10 это будет array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])).

import numpy as np
 
def my_array(N):
    x = np.arange(0,N)
    return np.flip(x,0)
    #np.sort(np.arange(0, N))[::-1]
    #return np.arange(N-1,-1,-1)
print(my_array(10))
print(my_array(15))
print(my_array(20))
