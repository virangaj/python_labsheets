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
    arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
    print(arr)
    c = np.zeros(5, int)
    print(c)
    
    arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

    print('Last element from 2nd dim: ', arr[1, -1])

convert()





