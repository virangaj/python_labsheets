def listing():
    print('List')
    list_1 = ['Kandy', 'Colombo', 'Galle', 'Jaffna', 'Ampara']
    print(list_1)
    print(type(list_1))
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
    print('Tupple')
    tuple1 = (1, 2, 3, 4, 5, 'Hello')
    print(type(tuple1))
    print(tuple1[3])


def setting():
    print('Set')
    set_1 = {1, 2, 3}
    print(set_1)
    print(type(set_1))


def dictionaries():
    print('Dictionaries')
    disc_1 = {'fisrt_name': 'Viranga', 'last_name': 'Jayawardana', 'age': 23}
    print(disc_1)
    print(type(disc_1))
    print(disc_1.keys())    # dict_keys(['fisrt_name', 'last_name', 'age'])
    print(disc_1.values())  # dict_values(['Viranga', 'Jayawardana', 23])
    # dict_items([('fisrt_name', 'Viranga'), ('last_name', 'Jayawardana'), ('age', 23)])
    print(disc_1.items())


dictionaries()
# setting()
# listing()
# tupling()
