import cmath

def quadratic():
    a = int(input('Enter value 1 : '))
    b = int(input('Enter value 3 : '))
    c = int(input('Enter value 2 : '))

    print('Equation is {}x2 + {}x + {}'.format(a,b,c))

    square = b**2-(4*a*c)

    sol_1 = (b*(-1) + cmath.sqrt(square))/(2*a)
    sol_2 = (b*(-1) - cmath.sqrt(square))/(2*a)
    
    print('solutions are {} and {}'.format(sol_1, sol_2))

quadratic()
    
