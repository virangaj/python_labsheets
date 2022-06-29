import random

def array_2d():
    array = [[0 for x in range(5)] for y in range(5)] 

    for i in range(0,5):
        for j in range(0,5):
            num = int(random.random() * 10)
            array[i][j] = num

    print(array)

def identity_mattrix():
    c = input("Enter number of column : ")
    r = input("Enter number of rows : ")

    array = [[o for x in range(c)] 0 for y in range(r)]
    for i in range(0,r):
        for j in range(0,c):
            if i == j:
                array[i][j] = 1
    
    print(array)


# array_2d()

