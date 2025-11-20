import numpy as np

before=np.array([[1,2,3,4],[5,6,7,8]])
print(before.shape)
''' This help us to reshape the array '''
after=before.reshape((4,2))
print(after)

after=before.reshape((2,2,2))
print(after)

''' VERTICALLY STACKING VECTORS/MATRICES '''

v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
print(v1)
print(v2)

print(np.vstack([v1,v2])) # this will stack/merge the arrays into 1
  
print(np.vstack([v1,v2,v1,v2,v1]))   # we can also do this

''' HORIZONTAL STACKING VECTORS/MATRICES '''

h1=np.array([1,2,3,4])
h2=np.array([5,6,7,8])
print(np.hstack([h1,h2,h2]))  # similar as vertically