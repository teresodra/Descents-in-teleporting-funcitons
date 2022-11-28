
import itertools

def first_min(perm):
    return all([perm[0] < elem2 for index2, elem2 in enumerate(perm) if index2 > 0])


def count_min(perm):
    mins = 0
    for index1, elem1 in enumerate(perm):
        if first_min(perm[index1:]):
            mins += 1

    return mins


def predict_descents(perm):
    descents = 0


def count_descents(perm):
    return sum([1 for elem1, elem2 in zip(perm[1:], perm[:-1]) if elem1 - elem2 < 0])


def creating_tp(perm, i=0):
    n = len(perm)
    i = max(i, perm.index(n - 1))
    if i < n:
        descents = 0
        for j in range(i, len(perm)):
            if first_min(perm[j:]):
                descents += creating_tp(perm, j + 1)
                if perm[j] != len(perm) - 1:
                    aux_perm = perm[:]
                    aux_perm[j] = len(perm) - 1
                    descents += creating_tp(aux_perm, j + 1)
                break

    else:
        descents = count_descents(perm)
    return descents


def total_descents_in_tp(n):
    """Return number of descents in all TP(n,n-1)."""
    l = list(range(n))
    total_descents = 0
    perms = itertools.permutations(l, n)
    for perm in perms:
        total_descents += creating_tp(list(perm))

    return total_descents