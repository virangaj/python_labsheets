# import keyword

# print(keyword.kwlist)
list_1 = ['Kandy', 'Colombo', 'Galle', 'Jaffna', 'Ampara']
tuple1 = (1, 2, 3, 4, 5, 'Hello')
set_1 = {1, 2, 3}


def forLoop(a):
    print(a)
    for i, n in enumerate(a):  # enumerate is used to get the index number
        print(i, n)


def forRange():
    for i in range(1, 6, 1):  # (start, stop, step) or (start, stop) method overloading
        if(i % 2 == 0):
            print('devid by two')
            break
        else:
            print('not devide by two')
    # for i in range(10, 6, -1): decrement value


# forLoop(list_1)
# forLoop(tuple1)
# forLoop(set_1)
forRange()
