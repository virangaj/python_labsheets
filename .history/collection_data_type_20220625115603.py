def listing():
    print('List')
    list_1 = ['Kandy', 'Colombo', 'Galle', 'Jaffna', 'Ampara']
    #['Kandy', 'Colombo', 'Galle', 'Jaffna', 'Ampara', 'Kaluthra', 'Kagalle', 'Matara', 'Amalangoda']
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
    print(tuple1)  # (1, 2, 3, 4, 5, 'Hello')


def setting():
    print('Set')
    set_1 = {1, 2, 3}
    print(set_1)    # {1, 2, 3}
    print(type(set_1))


def dictionaries():
    print('Dictionaries')
    disc_1 = {'first_name': 'Viranga', 'last_name': 'Jayawardana', 'age': 23}
    print(disc_1)
    print(type(disc_1))
    # dict_keys(['first_name', 'last_name', 'age']) shows as list
    print(disc_1.keys())
    # dict_values(['Viranga', 'Jayawardana', 23])   shows as list
    print(disc_1.values())
    print(disc_1.items())
    # dict_items([('first_name', 'Viranga'), ('last_name', 'Jayawardana'), ('age', 23)]) shows as tuple
    test = disc_1.copy()
    print(test)

    for key in disc_1.keys():
        print(key)

    for key, value in disc_1.items():
        print('Key : {} value : {} '.format(key, value))


dictionaries()
# setting()
# listing()
# tupling()
