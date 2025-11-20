import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(arr)

'''STATS'''
# min and max
print(np.max(arr))
print(np.min(arr))

print(np.max(arr,axis=1))  # This will give me the max and min of both row 1 and 2
print(np.min(arr,axis=1))

print(np.max(arr,axis=0))
print(np.min(arr,axis=0))

# sum
print(np.sum(arr))    

print(np.sum(arr,axis=1))

print(np.sum(arr,axis=0))
arr2=np.full((2,3),99)
print(arr2)
print(np.sum([arr,arr2]))  # it will give the total of all elements of the whole array/matrix

# mean and meadian
print(np.mean(arr))  
print(np.median(arr))  
print(np.mean(arr2))  
print(np.median(arr2))  

# standard deviation

print(np.std(arr))
print(np.std(arr2))












