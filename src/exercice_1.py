import numpy as np
import sympy as sym

n = sym.Symbol('n')
t = sym.Symbol('t')

# Exercice 1.1
def ex1_1():
    f1 = 0
    f2 = 1

    tmin1 = -1 * np.pi
    tmax1 = np.pi

    return (
        sym.Piecewise(
        (f1, ((tmin1 < t) & (t < 0))),
        (f2, ((0 <= t) & (t < tmax1)))
        ),
        tmin1,
        tmax1
    )



# Exercice 1.2
def ex1_2():
    f1 = 1
    f2 = t

    tmin2 = -1
    tmax2 = 1

    return (
        sym.Piecewise(
        (f1, ((tmin2 < t) & (t < 0))), 
        (f2, ((0 <= t) & (t < tmax2)))
        ),
        tmin2,
        tmax2
    )

# Exercice 1.3
def ex1_3():
    f1 = 0
    f2 = t ** 2

    tmin3 = -1 * np.pi
    tmax3 = np.pi

    return (
        sym.Piecewise(
        (f1, ((tmin3 < t) & (t < 0))),
        (f2, ((0 <= t) & (t < tmax3)))),
        tmin3,
        tmax3
    )


# Exercice 1.4
def ex1_4():
    f1 = t + np.pi

    tmin4 = -1 * np.pi
    tmax4 = np.pi

    return (
        sym.Piecewise(
        (f1, ((tmin4 < t) & (t < tmax4)))
        ),
        tmin4,
        tmax4
    )


# Exercice 1.5
def ex1_5():
    f1 = 0
    f2 = sym.sin(t)

    tmin5 = -1 * np.pi
    tmax5 = np.pi

    return (
        sym.Piecewise(
        (f1, ((tmin5 < t) & (t < 0))),
        (f2, ((0 <= t) & (t < tmax5)))
        ),
        tmin5,
        tmax5
    )

arr_fn = [ex1_1, ex1_2, ex1_3, ex1_4, ex1_5]