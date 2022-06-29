import random

def array_2d():
    array = [[0 for x in range(5)] for y in range(5)] 

    for i in range(0,5):
        for j in range(0,5):
            num = int(random.random() * 10)
            array[i][j] = num

    print(array)

def identity_mattrix():
    c = int(input("Enter number of column : "))
    r = int(input("Enter number of rows : "))
    array = [[0 for x in range(c)]  for y in range(r)]
    for i in range(0,r):
        for j in range(0,c):
            if i == j:
                array[i][j] = 1
    
    print(array)


# array_2d()
identity_mattrix()