def listing():
    list_1 = ['Kandy', 'Colombo', 'Galle', 'Jaffna', 'Ampara']
    print(list_1)
    list_2 = 'Kaluthra'
    list_3 = ['Kagalle', 'Matara', 'Amalangoda']
    list_1.append(list_2)
    print(list_1)
    list_1.extend(list_3)
    print(list_1)
    print(list_1[1])
    print(list_1[-1])
    print(list_1[1:3])


def tupling():
    tuple1 = (1, 2, 3, 4, 5, 'Hello')
    print(tuple1[3])


# listing()
tupling()
