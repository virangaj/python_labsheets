# area of a rectanle
def area_rectangle():
    height = input('Enter Height : ')
    width = input('Enter Width : ')
    return int(width)*int(height)


print('Area of a rectangle : ', area_rectangle())

# Area of a circle


def area_circle():
    radius = input('Enter radius : ')

    return 2*22/7*int(radius)


print('Area of a circle : ', area_circle())


# area of a triangle
def area_triangle():
    height = input('Enter height : ')
    base = input('Enter base : ')
    return int(height)*int(base)/2


print('Area of a triangle : ', area_triangle())

# area of a parallelogram


def area_parallelogram():
    height = input('Enter height : ')
    base = input('Enter base : ')
    return int(height)*int(base)/2


print('Area of a parallelogram : ', area_parallelogram())
