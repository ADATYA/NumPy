'''
1.rand   () : The function is used to generate a random value between 0 to 1.
2.randm  () : The function is used to generate a rendom value close to zero,This may return +ve and -ve number as well.
3.ranf   () : 
4.randint() :

'''
#1. Rand():
import numpy as np 

var= np.random.rand(4)
print(var)

print('\n')
var1 = np.random.rand(2,5)
print(var1)

print('\n')

#2.Rendn():
#  
import numpy as np
varb= np.random.randn(5)
print(varb)

print('\n')

#3.Ranf():
var3=np.random.ranf(4)
print(var3)

#4.Randint():
var4=np.random.randint(5,20,5)
print(var4)