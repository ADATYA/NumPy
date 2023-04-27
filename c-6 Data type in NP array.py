#Data Type:
import numpy as np 
var=np.array([1,2,3,4,5])
print("Data type : " ,var.dtype) # numpy represent [dtype]

print()

var=np.array([1.3,2.5,3.7,4.8,5.9])
print("Data type : " ,var.dtype) # numpy represent [dtype]

print()

var=np.array(['bikrom','roy','sporsho'])
print("Data type : " ,var.dtype) # numpy represent [dtype]

print()

var=np.array([1,2,3,'bikrom','roy'])
print("Data type : " ,var.dtype) # numpy represent [dtype]

print()

var=np.array([1,2,3,4,5],dtype = np.int8)
print("Data type : " ,var.dtype) # numpy represent [dtype]
print()
var=np.array([1,2,3,4,5],dtype=np.int16)
print("Data type : " ,var.dtype) # numpy represent [dtype]
print()
var=np.array([1,2,3,4,5],dtype=np.int32)
print("Data type : " ,var.dtype) # numpy represent [dtype]
print()
var=np.array([1,2,3,4,5],dtype=np.int64)
print("Data type : " ,var.dtype) # numpy represent [dtype]

print()

var=np.array([1,2,3,4,5],dtype=np.int16)
print("Data type : " ,var.dtype) # numpy represent [dtype]
print(var)

print()

# int to convert float :

var1=np.array([1,2,3,4,5],dtype= 'f')
print("Data type : " ,var1.dtype) # numpy represent [dtype]

print(var)

print()

var=np.array([1,2,3,4,5],dtype='B')
print("Data type : " ,var.dtype) # numpy represent [dtype]
print(var)

print() 

# data type as a function : 

var=np.array([1,2,3,4,5])
function = np.float32(var)
print("Data type : " ,var.dtype) # numpy represent [dtype]
print("Data type : " ,function.dtype) # numpy represent [dtype]
print(var)
print(function)

print()
 
var=np.array([1,2,3,4,5])
function = np.float32(var)

new_one = np.int_(function)

print("Data type : " ,var.dtype) # numpy represent [dtype]
print("Data type : " ,function.dtype) # numpy represent [dtype]
print("Data type : " ,new_one.dtype) # numpy represent [dtype]

print(var)
print(function)
print(new_one)


# Directly convert data type:

var5=np.array([1,2,3,4,5])
new_list = var5.astype(float)
print()
print(new_list)





