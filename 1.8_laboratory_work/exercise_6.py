# "Дана матрица matrix. Напишите код, который будет транспонировать её
# (то есть, делать из строк столбцы)
# import pymatrix

matrix = [ 
    [0,1,2,4,8], 
    [6,2,2,1,9], 
    [3,3,3,3,3], 
    [4,6,7,1,2], 
    [5,7,3,4,0] 
]

zipped_rows = zip(*matrix)
# print(zipped_rows) #<zip object at 0x000002371082AEC0>
transponse_matrix = [list(row) for row in zipped_rows]
print (transponse_matrix)