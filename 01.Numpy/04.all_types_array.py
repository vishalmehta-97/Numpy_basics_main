import numpy as np

'''All 0s Matrix'''

a=np.zeros(5)
print(a)

ar=np.zeros([5,5])
print(ar)
 
arr=np.zeros([2,3,3])
print(arr)

arrr=np.zeros([2,3,3,2])
print(arrr)


'''All 1s Matrix'''
 
b=np.ones(2)
print(b)

br=np.ones([2,2])
print(br)

brr=np.ones([2,3,3])
print(brr)

# you can also specify datatype
brrr=np.ones([2,3,3],dtype='int32')
print(brrr)
# basic attributes we can check 
print(brrr.dtype)
print(brrr.shape)
print(brrr.ndim)
print(brrr.itemsize)
print(brrr.nbytes)

'''Any other number matrix'''

arr=np.full((2,3),99)
print(arr)

'''Any other number matrix using like function'''

arr=np.full_like(brrr,4)    # it will make array like mentioned array and el
print(arr)

'''OR'''

arr=np.full(brrr.shape,4)
print(arr)

print("bk")

'''Random decimal numbers matrix'''

arr=np.random.rand(2,3) # when you want decimal no.(0to1)
print(arr)
arr3=np.random.rand(2,2,3)
print(arr3)

arr_brrr=np.random.random_sample(brrr.shape)  # Here brrr is another array/matrix of (2,3,3) and we're copying its shape and giving random no to it
print(arr_brrr)

'''Random integer value matrix'''

int_arr=np.random.randint(10,size=(3,3))   # Here 10 is the perameter value of matrix/array
print(int_arr)

int_arrr=np.random.randint(4,7,size=(2,3,3))  # here we are putting interval in the perameter 4 to 7
print(int_arrr)

int_arrr=np.random.randint(-2,4,size=(3,3))  # we can also choose negative numbers here
print(int_arrr)

'''IDENTITY [I] Matrix'''

iarr=np.identity(3)
print(iarr)


'''TO REPEAT AN ARRAY'''

# for 1D array
R_arr1 = np.array([1, 2, 3])
repeated1 = np.repeat(R_arr1, 3)  # We use this to repeat any array's element in this ex. we're repeating 1,2,3 for 3 times like 111222333
print(repeated1)

# for 2d array

R_arr2 = np.array([[1, 2, 3]])
repeated2 = np.repeat(R_arr2, 3,axis=0)
print(repeated2)



'''QUES : Make a 5x5 matrix where all the outer elements are 1 and the middle most  element is 9'''
'''ANS'''

array=np.zeros([5,5])
print(array)

array[:,(0,4)]=1
print(array)

array[(0,4),:]=1
print(array)

array[2,2]=9
print(array)

''''another solution here'''

output=np.ones([5,5])
print(output)

z=np.zeros([3,3])
z[1,1]=9
print(z)
 ## Be careful when copying arrays!!!!
output[1:4,1:4]=z      
print(output)

''''''
'''Copying Of Array'''
a=np.array([1,2,3])
b=a.copy()    # using this(.copy()) will help to copy the array and it will also help if we do some changes in the copied array by not effecting the original array
print(a)
b[0]=10
print(b)




