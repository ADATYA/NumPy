import numpy as np # [as -> alias]

# create a Array :
x=np.array([1,2,3,4,5])
print(x)
print(type(x))

# create a List :
y=([1 ,2 ,3 ,4, 5 ,6 ])
print(y)
print(type(y))

import numpy as np
#%timeit [j**4 for j in range(1,9)]

import numpy as np
#%timeit np.arrange(1,9)**4

#Note : jodi single line code er time dhakte chai tobe [%timeit] hobe.
# aber puro code er time dhakte chile [%%timeit] use korbo.