import numpy as np

a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

# Get a specific element [r,c]  
print(a[1,5])

# Or in negative indexing same as list
print(a[-1,-2])

# Get a specific row
print(a[0,:])

# Get a specific column
print(a[:,3])

# getting a little more fancy [startindex:endindex:stepsize]

print(a[1,2::2])
print(a[-1,-5::2])

print(a[-1,-1:-6:-2]) # reverse in this

print(a[-2,-1:-6:-2])