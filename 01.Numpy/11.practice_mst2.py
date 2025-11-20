import numpy as np

arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr))

a=np.zeros([2,2,2])
print(a)


b=np.ones([2,2,2])
print(b)


f=np.full([3,3],99)
print(f)

c = np.arange(0, 10, 2)        
print(c)
c = np.arange(0, 10)        
print(c)


d = np.linspace(0, 1, 5)
print(d)

# slicing
print(arr[1:3])
print(arr[1:4:2])
print(arr[::2])
print(arr[:])
print(f[1:3,1:3])

ar=np.full((4,2),99)
print(ar)

print(ar[:,0])

arrrr=np.array([[100,2,3,4,5],[6,7,8,9,0]],dtype='bool')
print(arrrr)
print(arrrr.dtype)


a=np.array([1.1,2.1,3.1])
newa=arr.astype(int)
print(newa)
print(newa.dtype)

n1=np.ones([3,3],dtype='int32')
print(n1)
print(n1.itemsize)
print(n1.nbytes)

n1.shape=(9,1)
print(n1)

aa=np.array([1,2,3,4,5,6,7,8,9,3,4,6])
print(aa)
newaa=aa.reshape(3,4)
print(newaa)

# for i in aa:
#     for j in i:
#         print(j)

array=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.array_split(array,3))

print(array[0])
print(array[1])
print(array[2])

x=np.where(aa==6)
print(x)

y=np.sort(aa)
print(y)