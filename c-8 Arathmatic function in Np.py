'''
np.min(X)
np.max(X)
np.argmin(X)
np.sqrt(X)
np.sin(X)
np.cos(X)
np.cumsum(X)

'''

import numpy as np
var = np.array([1,2,3,4,5,6,7,8])
print("The minimum value :",np.min(var),np.argmin(var))

print()

print("The maximum value :",np.max(var),np.argmax(var))

print()

print("The argument minimum value :",np.argmin(var))

print()

print("The squreroot value :",np.sqrt(var))

print()

print("The Sin value :",np.sin(var))

print()

print("The Cos value :",np.cos(var))

print()

print("The cumsum value :",np.cumsum(var))

var1=np.array([[1,2,3],[5,7,9]])
print(np.min(var1,axis=0))
