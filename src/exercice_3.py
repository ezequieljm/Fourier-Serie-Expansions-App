import numpy as np
import sympy as sym

n = sym.Symbol('n')
t = sym.Symbol('t')

# Exercice 3.1
def ex3_1():
    f1 = -1
    f2 = 1

    tmin1 = (-1) * np.pi
    tmax1 = np.pi

    return (
        sym.Piecewise(
        (f1, ((tmin1 < t) & (t < 0))),
        (f2, ((0 <= t) & (t < tmax1)))
        ),
        tmin1,
        tmax1
    )

# Exercice 3.2
def ex3_2():
    f1 = np.abs(t)

    tmin2 = (-1) * np.pi
    tmax2 = np.pi

    return(
        sym.Piecewise(
        (f1, ((tmin2 < t) & (t < tmax2))),
    ),
        tmin2,
        tmax2
    )

# Exercice 3.3
def ex3_3():
    f1 = t ** 2

    tmin3 = -1
    tmax3 = 1

    return (
        sym.Piecewise(
        (f1, ((tmin3 < t) & (t < tmax3))),
    ),
        tmin3,
        tmax3
    )

# Exercice 3.4
def ex3_4():
    f1 = (np.pi ** 2) - t ** 2

    tmin4 = (-1) * np.pi
    tmax4 = np.pi

    return (
        sym.Piecewise(
        (f1, ((tmin4 < t) & (t < tmax4))),
    ),
        tmin4,
        tmax4
    )

# Exercice 3.5
def ex3_5():
    f1 = t - 1
    f2 = t + 1

    tmin5 = (-1) * np.pi
    tmax5 = np.pi

    return (
        sym.Piecewise(
        (f1, ((tmin5 < t) & (t < 0))),
        (f2, ((0 <= t) & (t < tmax5)))
    ),
        tmin5,
        tmax5
    )


arr_fn = [ex3_1,ex3_2,ex3_3,ex3_4,ex3_5]