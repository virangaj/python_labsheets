# import keyword

# print(keyword.kwlist)
list_1 = ['Kandy', 'Colombo', 'Galle', 'Jaffna', 'Ampara']
tuple1 = (1, 2, 3, 4, 5, 'Hello')
set_1 = {1, 2, 3}


def forLoop(a):
    print(a)
    for i, n in enumerate(a):
        print(i, n)


def forRange():
    for i in range(1, 6, 2):
        print(i)


# forLoop(list_1)
# forLoop(tuple1)
# forLoop(set_1)
forRange()
