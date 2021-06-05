import numpy as np
from sys import getsizeof
import random
from timeit import Timer

size = 1000000

temp = [-1.5, -1.2, 0.0, 2.1, 24.2]
X = [random.randint(0,200) for _ in range(size)]
Y = [random.randint(0,200) for _ in range(size)]

np_temp = np.array(temp)
np_X = np.array(X)
np_Y = np.array(Y)



def python():
    res = [X[i]+ Y[i] for i in range(size)]
    return res


def numpy():
    res = np_X + np_Y
    return res



timePython = Timer("python()", "from __main__ import python").timeit(10)
timeNP = Timer("numpy()", "from __main__ import numpy").timeit(10)

print(f"Size of python list: {getsizeof(X)}")
print(f"Size of NP Array: {getsizeof(np_X)}")
print(f"time for python was: {timePython}")
print(f"time for numpy was: {timeNP}")