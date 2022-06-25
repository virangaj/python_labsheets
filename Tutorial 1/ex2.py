def factorial():
    num = input('Enter number : ')
    n = int(num)
    a = 1
    while n >= 1:
        a *= n
        n -= 1
    return a


print(factorial())
