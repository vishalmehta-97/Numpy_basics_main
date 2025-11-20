import numpy as np
''' LOAD DATA FROM FILE '''

data=np.genfromtxt('numpy_prac_data.csv',delimiter=',')

print(data)                   # this will give the float values
print(data.astype('int32'))   # this will change the values type from float to int
'''or'''
data=data.astype('int32')
print(data)




''' BOOLEAN MASKING & ADVANCED INDEXING '''

print(data>50)      # It will give the boolean values about values that value is greater or less

print(data[data>50])      # it will give only the values which are greater than 50

any=np.any((data)>50,axis=0)    # it will give all the values(true or false) weather in the column (axis=0) any value is greater than 50 or not 
print(any)
all=np.all((data)>50,axis=0)      # it will give the vales that all the value is greater tha 50 in column
print(all)

# we can also do this for rows
print(np.any((data)>50,axis=1))     
print(np.all((data)>50,axis=1))     

# multiple condition
print((data>50) & (data<100))
print(~(data>50) & (data<100))  # this is is not condition means not greater than 50 and not smaller than 100




''' You can index with a list in nump'''

a=np.array([1,2,3,4,5,6,7,8,9])    
print(a[[1,5,8]])                   # you have to use 2 square bracket here to give indexing bcz we have to pass it as a list 


