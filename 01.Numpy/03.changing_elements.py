import numpy as np

a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

#change in a specific element
a[1,1]=90
print(a)

#change in column
a[:,3]=5
print(a)
'''or'''
a[:,2]=[30,100]
print(a)

## in 3-D array

arr=np.array([
    [[1,2],[3,4]],[[5,6],[7,8]]
    ])

print(arr)

# Get specific element
'''[block_index,row_index,column_index]''' 
print(arr[1,1,0])
print(arr[0,1,1])

print(arr[:,1,:])  # it will give 2nd row from the both blocks
print(arr[:,:,1])  # it will give 2nd column from the both blocks

# if we want to replace values
print('hello')
arr[:,1,:]=[[9,9],[8,8]]
print(arr)


arr[1,0,0]=9
print(arr)

  






