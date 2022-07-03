from ctypes.wintypes import INT
from tokenize import String
import numpy as np

# convert normal array to numpy array
def convert():
    a = [1,2,3,4,5]
    print(type(a))
    # convert in to numpy array
    b = np.array([1,2,3])
    print(type(b))
    # create new array with zeros

    c = np.zeros(5, ,dtype=complex)
    print(c)


convert()





