import random  
import time
import numpy as np

# Question 1

# a
# create 2D array
def array_2d():
    array = [[0 for x in range(5)] for y in range(5)] 

    for i in range(0,5):
        for j in range(0,5):
            num = int(random.random() * 10)
            array[i][j] = num

    print(array)

#  b
# create indentity mattrix
def identity_mattrix():
    c = int(input("Enter number of column : "))
    r = int(input("Enter number of rows : "))
    if r == 0 or c == 0:
        print("Array size is empty")
    else:
        array = [[0 for x in range(c)]  for y in range(r)]
        for i in range(0,r):
            for j in range(0,c):
                if i == j:
                    array[i][j] = 1
                else:
                    array[i][j] = 0
        print(array)

    
    
# c / d
# multiply arrays
def mattrix_multiply():
    print("------------Create mattrix 1------------")
    array_1 = generate_mattrix()
    print("------------Create mattrix 2------------")
    array_2 = generate_mattrix()
    
    st = time.time()
    if len(array_1) == len(array_2[0]):
        print('Mattixies can be multiply')
        convert_nparr(array_1, array_2)
        answer = []
        for i in range(0, len(array_1)):
            temp = []
            for j in range(0, len(array_2[0])):
                total = 0
                l = 0
                for k in range(0, len(array_1[0])):
                    total +=  array_1[i][k] * array_2[l][j]
                    l += 1  
                temp.append(total)
            answer.append(temp)
        time.sleep(3)
        print(answer)
    else:
        print('Mattixies cannot be multiply')
    et = time.time()

    print('Execution time : {}'.format(et-st-6))

# generate mattrix using user inputs
def generate_mattrix():
    r = int(input("Enter number of rows : "))
    c = int(input('Enter number of columns : '))
    
    if r == 0 or c == 0:
        print("Aray size is empty")
    else: 
        array = [[0 for x in range(c)] for y in range(r)]
        for i in range(0, r):
            for j in range(0, c):
                num = int(input("Enter value for {} {} index : ".format(i,j)))
                array[i][j] = num
        return array
        

# Question 2

# a 
def create_numArr():
    '''we can use np.zeros_like() method for that we have to initialize a array with given length'''
    arr = np.zeros(10)
    print(arr)

# c d
# convert in to numpy array
def convert_nparr(arr1, ar22):
    numarr1 = np.array(arr1)
    numarr2 = np.array(ar22)

    st = time.time()
    time.sleep(3)
    dotnp = np.dot(numarr1,numarr2)
    et = time.time()
    print(dotnp)
    print(et-st-3)

    #sustract two arrays
    arr3 = np.subtract(numarr1,numarr2)
    print(arr3)
    
    #add two arrays
    arr3 = np.add(numarr1,numarr2)
    print(arr3)

# e f 
def array_with_ele():
    arr = np.array([4,7,9,-1,3,5,8])
    print('max : {}'.format(np.max(arr)))
    print('min : {}'.format(np.min(arr)))
    print('sum : {}'.format(np.sum(arr)))
    print('Mimimun index : {}'.format(np.argmin(arr)))

# g h i j k i 
def question_g():
    array_A = np.arange(5,23,2)
    array_B = np.linspace(5,9,9)
    # Change the previous array(B) so that it has a shape of 3x3 instead.
    array_C = np.reshape(array_B,(3,3))
    cos_array = np.cos(array_A)
    print(array_A)
    print(array_B)
    print(array_C)
    # Find the cosine of each index of the array(A).
    print(cos_array)
    # Display the values of the array (A) of indices 2 to 6.
    print(array_A[2:6])
    # Display all the values of column 1 of the array (B).
    print(array_C[:,0])

def question_n():
    arr_1 = np.random.radint(4)
    print(arr_1)



# array_2d()
# identity_mattrix()
# mattrix_multiply()
# create_numArr()
# array_with_ele()
# question_g()
question_n()
