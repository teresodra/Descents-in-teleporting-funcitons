"""Code needed to compute the number of descents in TP(n,n-1) we predict theoretically."""

import math

def d_in_dtp(n):
    average_descents = 0
    for k in range(n):
        average_descents += aveg_descents_in_perms(k)*(n-k) + x(n-k)
        # x(n-k) stands for the average number of descents that each permutation that starts with the biggest number has
    total_descents = math.factorial(n-1)*average_descents
    return total_descents

def x(n):
    """Counts the average number of descents that each permutation that starts with the biggest number has."""
    if n>1:
        return (n-1) + x(n-1)/(n-1) + y(n-1)
    else:
        return 0


def y(n):
    if n>1:
        return y(n-1) + x(n)/n + 1/2*(n-2)
    else:
        return 0

def aveg_descents_in_perms(n):
    if n == 0:
        return 0
    else:
        return (n-1)/2
