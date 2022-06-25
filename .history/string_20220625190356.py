def string_tuto():
    name = 'Viranga'
    last = 'pasindu'
    full = name+last
    print(name+last) #concat
    print(name[:3]) #Vir 0th to 3rd character count as 1,2,3
    print(name[2:5]) #ran include 1 and exclude 5
    print(name*5)
    print('a' not in name) #false
    print('a' in name) #true
    a = str(4) #typecast
    print(type(a))
    print(name.upper()) #to uppercase -> VIRANGA
    print(name.lower()) #to lowercase -> viranga
    print(name.swapcase()) #swap case -> vIRANGA
    print(last.isupper())

string_tuto()
