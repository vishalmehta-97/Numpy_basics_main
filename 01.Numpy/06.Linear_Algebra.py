import numpy as np

arr=np.ones([2,3])  # It's a 2x3 matrix 
print(arr)

brr=np.full([3,2],2)   # It's a 3x2 matrix 
print(brr) 

'''So multiplication of these two matrix possible bcz 2x(3) and (3)x2 both matches so the final matrix after multiplication would be 2x2  '''
print(np.matmul(arr,brr))   # with this we can do this 

c=np.identity(3)
print(c)
'''This is how we can get determinant of any matrix and we can find the determinant of only square matrices '''
print(np.linalg.det(c))

## with this we get INVERSE Of the matrix
print(np.linalg.inv(c))

## TRACE (sum of diagonal elements)
print(np.trace(c))