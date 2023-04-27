import numpy as n

m=[1,2,3,4,5,6]
a = n.array(m)
print (a)
print(type(a))
print(a.ndim)


# Appand Function:

list=[]

for i in range(1,3):
    int_1=input("Enter value:")
    list.append(int_1)
    # print(int_1)
    print(n.array(list))
    

print('\n\n')
sub=[]

for i in range(1,4):
    
    mock=input("Enter:")
    sub.append(mock)
    print(n.array(sub))


                            ## Dimention of array ##
'''
1D Array -->> [1 2 3 4 7]
2D Array -->> [[1 2 3 4 7]]
3D Array -->> [[[1 3 4 7]]]
Higher Dimentional Arrays -->> 

[ndim] function use kore dimention chacke kora jay.

'''

# l=n.array([[1,2,3,4,5,7],[2,3,4,5]])  #2D
# m=n.array(l)
# print(m)
# print(m.ndim)

# print()

# a2=n.array([[1,2,3,4,5,7],[1,2,3,4,5,7]])  #2D
# print(a2)
# print(a2.ndim)


# lst=n.array([[[1,2,3,4,6,5],[1,2,3,4,6,5],[1,2,3,4,6,5]]]) #3D
# m=n.array(lst)
# print(m)
# print(m.ndim)

# print()

# a3=n.array([[[1,2,3,4,6,5],[3,4,5,6,],[56,56,76,]]]) #3D
# print(a3)
# print(a3.ndim)

ar2=n.array([[1,2,3,4],[1,2,3,4]])  #2D
print(ar2)
print(ar2.ndim)

print()

ar3=n.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])  #2D
print(ar3)
print(ar3.ndim)

print()

arn = n.array([1,2,3],ndmin = 10) #ndmin use korle hight dimention array nawa jay.
print(arn)
print(arn.ndim)

'''
Note: 
        Array value gulo list er moto print kore.
jodi array er vetor data kom basi hoy ba alada hoy tahole error asbe.


''' 