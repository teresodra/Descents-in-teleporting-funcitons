from theoretical_counting import x
from theoretical_counting import y

def x_guess(n):
    if n == 0:
        return 0
    else:
        return 1/2*n**2 - 1/2*n


def check_x(m):
    for n in range(m):
        if x_guess(n) == x(n):
            print('Works for ' + str(n))
        else:
            print('Noooooooooo')

def y_guess(n):
    if n == 0:
        return 0
    else:
        return 1/2*(n - 1)**2


def check_y(m):
    for n in range(m):
        if y_guess(n) == y(n):
            print('Works for ' + str(n))
        else:
            print('Noooooooooo')



check_y(10)