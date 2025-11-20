import numpy as np

matrix=np.arange(1,31).reshape(6,5)
print(matrix)

print(matrix[2:4,0:2])

print(matrix[[0,1,2,3],[1,2,3,4]])

print(matrix[[0,4,5],3:])