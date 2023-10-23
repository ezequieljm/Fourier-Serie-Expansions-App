import exercice_1 as ex1
import exercice_3 as ex3
import exercice_4 as ex4
import superior_func as sup
import superior_func_by_intervals as sup_in


import os
from platform import system
import numpy
import sympy


def terminal_clear():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def menu_g12():
    while True:
        terminal_clear()
        print("\t\tGraficador de Serie de Fourier\n")
        print("Ingrese el número del ejercicio")
        print("Ejercicio 1")
        print("Ejercicio 3")
        print("Ejercicio 4")
        print("Salir >>> 5")
        
        option = input()
        
        if option == "1":
            while True:
                terminal_clear()
                print("Ingrese la función a calcular la Serie de Fourier")
                print("1) ")
                print("2) ")
                print("3) ")
                print("4) ")
                print("5) ")

            
                option = input()

                terminal_clear()

                ft, tmin, tmax = ex1.arr_fn[int(option) - 1]()
                sup.superior_func(ft,tmin,tmax,1,int(option))       
                print(f"Continuar con los ejercicios del punto {option} presione Enter")
                print("Seleccionar otro Ejercicio ingrese 2")
                opt = input()
                if opt == "2": break

        elif option == "3":
            while True:
                terminal_clear()
                print("Ingrese la función a calcular la Serie de Fourier")
                print("1) ")
                print("2) ")
                print("3) ")
                print("4) ")
                print("5) ")
            
                option = input()

                terminal_clear()

                ft, tmin, tmax = ex3.arr_fn[int(option) - 1]()
                sup.superior_func(ft,tmin,tmax,3,int(option))       
                print(f"Continuar con los ejercicios del punto {option} presione Enter")
                print("Seleccionar otro Ejercicio ingrese 2")
                opt = input()
                if opt == "2": break

        elif option == "4":
            while True:
                terminal_clear()
                print("Ingrese la función a calcular la Serie de Fourier")
                print("1) ")
                print("2) ")
                print("3) ")
                print("4) ")
            
                option = input()

                terminal_clear()

                ft, val ,tmin, tmax = ex4.arr_fn[int(option) - 1]()
                sup_in.superior_func_by_intervals(ft,val,tmin,tmax,4,int(option))       
                print(f"Continuar con los ejercicios del punto {option} presione Enter")
                print("Seleccionar otro Ejercicio ingrese 2")
                opt = input()
                if opt == "2": break
        else:
            terminal_clear()
            print("Bye")
            break
    