import numpy as np
import sympy as sym

n = sym.Symbol('n')
t = sym.Symbol('t')


# Exercice 4.1
def ex4_1():

    f1 = 1
    f2 = 0

    tmin1 = 0
    tmax1 = 1

    return (
        sym.Piecewise(
        (f1, ((tmin1 < t) & (t < 0.5))),
        (f2, ((0.5 <= t) & (t < tmax1)))
    ),
        False,
        tmin1,
        tmax1
    )

# Exercice 4.2
def ex4_2():
    tmin2 = 0
    tmax2 = np.pi/2

    f1 = sym.cos(t)

    return (
        sym.Piecewise(
        (f1, ((tmin2 < t) & (t < tmax2))),
    ),
        True,
        tmin2,
        tmax2
    )

# Exercice 4.3
def ex4_3():
    f1 = t
    f2 = np.pi - t

    tmin3 = 0
    tmax3 = np.pi

    return (
        sym.Piecewise(
        (f1, ((tmin3 < t) & (t < np.pi/2))),
        (f2, ((np.pi/2 < t) & (t < tmax3)))
    ),
        False,
        tmin3,
        tmax3
    )


# Exercice 4.4
def ex4_4():
    f1 = t
    f2 = 1

    tmin4 = 0
    tmax4 = 2
    
    return (
        sym.Piecewise(
        (f1, ((tmin4 < t) & (t < 1))),
        (f2, ((1 < t) & (t < tmax4)))
    ),
        False,
        tmin4,
        tmax4
    )


arr_fn = [ex4_1,ex4_2,ex4_3,ex4_4]