'''
Array filled with 0's
Array filled with 1's
Create an  empty array
An array with a range of element 
Array diagonal element filled with 1's
Create an array with values that are spaced linerly in a specifide interval.

'''

# Array filled with 0's:

import numpy as np 

ar_zero=np.zeros(4)
ar_zero1=np.zeros((3,3))
print(ar_zero)
print('\n')
print(ar_zero1)

print('\n')
# Array filled with 1's :

ar_one=np.ones(7)
print(ar_one)
print('\n')

ar_one4=np.ones((3,5))
print(ar_one4)

print('\n')
# Create an  empty array:

ar_em=np.empty(1)
print(ar_em)

print('\n')
# An array with a range of element :

ar_arg = np.arange(7)
print(ar_arg)

print('\n')
#Array diagonal element filled with 1's :

ar_dig = np.eye(3)  #Diagonal er jonno [eye function] use korbo.
print(ar_dig)
print(ar_dig.ndim)

ar_dig1 = np.eye(3,4)  #Diagonal er jonno [eye function] use korbo.
print(ar_dig1)
print(ar_dig1.ndim)

print('\n')

# Create an array with values that are spaced linerly in a specifide interval : 

ar_linsps=np.linspace(0,20,num=5)
print(ar_linsps)