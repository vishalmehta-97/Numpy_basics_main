import numpy as np
arr1=np.array([1,2,3,4])
print(arr1)

'''DOING SOME BASIC ARITHMETIC OPERATION'''
# Add in matrix
print(arr1+2)
 # Subtract in Matrix
print(arr1-2)
#multiply
print(arr1*2)
#Divide
print(arr1/2)

'''ADDING OF TWO MATRIX'''  #(SHAPE SHOULD BE SAME OF BOTH MATRIX/ARRAY)
arr2=np.array([1,0,1,0])
result=arr1+arr2
print(result)
'''or'''
print(arr1 + arr2)

'''SUBTRACTION OF TWO MATRIX'''
print (arr1-arr2)

'''MULTIPLICATION OF MATRICES'''
print(arr1*arr2)

'''POWER'''
print(arr1**2)
print(arr2**2)

'''TAKE THE SIN OF ALL VAUES'''
print(np.sin(arr1))      # this gives the sin value of all elmements in A 

'''FOR COS'''
print(np.cos(arr1))

'''FOR TAN'''
print(np.tan(arr1))





