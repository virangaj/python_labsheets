from ctypes.wintypes import INT
from tokenize import String
import numpy as np
import random
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
    
    # negative indexing
    arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
    print(arr[1, 1:4])
    print('Last element from 2nd dim: ', arr[1, -3])

    # array slicing
    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    # print(arr[1:5])
    # print(arr[4:])
    # print(arr[:4])
    # print(arr[-3:-1])
    # x = arr.copy()
    # y = arr.view()

    # split array
    newarr = np.array_split(arr, 4)

    print(newarr)

    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

    # newarr = np.array_split(arr, 3) 
    newarr = np.random.normal(10,5,5).astype(int)

    # unifrom array
    arr2 = np.linspace(0,1,10)
    arr2 = np.random.randint(10, size=(2,3))
    print(arr2)

convert()





