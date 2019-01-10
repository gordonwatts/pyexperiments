# Try out numba vectorize

from numba import vectorize, float64, int32
import numpy as np

@vectorize([float64(float64, float64)])
def f(x,y):
    return x + y

a = np.arange(60000000)
print (a)
print (f(a,a))
print (a+a)

@vectorize([int32(int32)])
def f2(x):
    return 2+x

print (f2(a))
print (2+a)
