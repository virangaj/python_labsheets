def fibonacci():
    num = int(input('Enter Number : '))
    n1, n2 = 0, 1
    count = 0

    if num == 0:
        print(n1)
    elif num == 1:
        print(n2)
    else:
        while count < num:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1


fibonacci()
