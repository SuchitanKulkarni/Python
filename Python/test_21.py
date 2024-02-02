# Initializing Numpy Array :
# Initializing Numpy Array as Zero :

import numpy as np
n1 = np.zeros((2,3))
l1 = n1
print(l1)
print(type(l1))

n2 = np.zeros((10,10))
l2 = n2
print(l2)
print(type(l2))
# Initializing Numpy as same Number :

import numpy as np
n1 = np.full((4,4),(9))
l3 = n1
print(l3)
print(type(l3))

import numpy as np
n2 = np.full((7,7),66)
l4 = n2
print(l4)
print(type(l4))

# Initializing Numpy Array within a Range :
import numpy as np
n3 = np.arange(50,100)
l5 = n3
print(l5)

import numpy as np
n4 = np.arange(50,400,18)
l6 = n4
print(l6)
print(type(l6))

# Initializing Numpy Array with Random Numbers :

import numpy as np
n5 = np.random.randint(1,700,50)
l7 = n5
print(l7)
print(type(l7))
