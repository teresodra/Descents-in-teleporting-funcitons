import math
from empirical_counting import total_descents_in_tp
from theoretical_counting import d_in_dtp

def empirical_vs_theoretical(m):
    for n in range(3,m):
        if total_descents_in_tp(n)==d_in_dtp(n):
            print('WOW! ' + str(total_descents_in_tp(n)) + ' is equal to ' + str(d_in_dtp(n)))
        else:
            print('NOOOOOOOOOOOOOOOOO, it does not work for ' + n + ', ' + str(total_descents_in_tp(n)) + ' is not equal to ' + str(d_in_dtp(n)))

def expected_vs_theoretical(m):
    for n in range(3,m):
        if math.factorial(n)*n*(n-1)/4==d_in_dtp(n):
            print('WOW! ' + str(math.factorial(n)*n*(n-1)/4) + ' is equal to ' + str(d_in_dtp(n)))
        else:
            print('NOOOOOOOOOOOOOOOOO, it does not work for ' + n + ', ' + str(math.factorial(n)*n*(n-1)/4) + ' is not equal to ' + str(d_in_dtp(n)))

empirical_vs_theoretical(9)
expected_vs_theoretical(20)