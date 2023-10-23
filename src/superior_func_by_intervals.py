import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def superior_func_by_intervals(fn,sine_true,l_min,l_max,exercise,dot):

    n = sym.Symbol('n')
    t = sym.Symbol('t')

    L = l_max - l_min
    T = 2 * L
    w0 = (2 * np.pi)/T

    # We create a time vector for the graph
    v_time = np.linspace(-1*l_max,l_max,1000)

    f = sym.lambdify(t,fn)
    fg = f(v_time)
    plt.plot(v_time, fg, label = "f(t)")

    # Coefficients

    if sine_true:
      #a0
      a0 = 0

      #an
      an = 0

      # bn
      fbn_integrate = fn * sym.sin(n * w0 * t)
      bn = (2/T) * 2 * sym.integrate(fbn_integrate,(t,l_min,l_max))
      bn = sym.simplify(bn)
      print("bn =")
      sym.pprint(bn)
    else:
      # a0
      fa0_integrate = fn
      a0 = (2/T) * 2 * sym.integrate(fa0_integrate,(t,l_min,l_max))
      print("a0 = ")
      sym.pprint(a0)

      #an
      fan_integrate = fn * sym.cos(n * w0 * t)
      an = (2/T) * 2 * sym.integrate(fan_integrate,(t,l_min,l_max))
      an = sym.simplify(an)
      print("an =")
      sym.pprint(an)

      #bn
      bn = 0

    # We define the Harmonics

    #harmonics = 2
    v_harmonics = [2,10,30]

    for j in v_harmonics:
        serie = 0
        for i in range(1,j + 1):
            # We evaluate the coefficients for each harmonics
            if bn == 0:
              an_c = an.subs(n,i)
              bn_c = 0
            else:
              an_c = 0
              bn_c = bn.subs(n,i)

            if abs(an_c) < 0.0001: an_c = 0
            if abs(bn_c) < 0.0001: bn_c = 0

            serie = serie + (an_c * sym.cos(i * w0 * t))
            serie = serie + (bn_c * sym.sin(i * w0 * t))

        serie = (a0 / 2) + serie
        # print("f(t) =")
        # sym.pprint(serie)

        # Graph
        fserie = sym.lambdify(t,serie)

        # We evaluate the functions
        fserieg = fserie(v_time)

        plt.plot(v_time, fserieg, label= str(j) + " Armónicos")
        plt.xlabel('Time')
        plt.ylabel('Y')
        plt.legend()
        plt.title('Expansión en Series de Fourier. Ejercicio ' + str(exercise) + '.' + str(dot))
        plt.grid()