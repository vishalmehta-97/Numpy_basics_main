import numpy as np

# The Basics

a=np.array([1,2,3,4])
print(a)

b=np.array([[9.0,8.0,7.0],[6.0,7.0,2.0]])
print(b)


# Get Dimension

print(a.ndim)
print(b.ndim)


# Get Shape

print(a.shape)
print(b.shape)

# Get Type

print(a.dtype)
print(b.dtype)

c=np.array([21,22,23],dtype='int16')  #to do change in datatype and size
print(c)
print(c.dtype)


# give size of array in bytes
print(a.itemsize)
print(b.itemsize)
print(c.itemsize)

# Get total size
print(a.nbytes)
print(b.nbytes)
print(c.nbytes)

# You can index with a list in numpy 
a=np.array([1,2,3,4,5,6,7,8,9])    
print(a[[1,5,8]])   # you have to use 2 square bracket here to give indexing







































# arr=np.array([ i for i in range (1,10)])
# print(arr)
# squares =np.array([x**2 for x in range(5)])

# arraone=np.ones((3,3))

# e = np.arange(1,100,2) 


# arr = np.linspace(0, 10, 2)
# print(arraone)

# print(squares)  

# print(type(a))
# print(type(squares))
# print(type(arr))
# print(e)
# print( type(arr))