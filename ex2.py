"""Ejercicio de arreglo de 1 hasta n números, se identificarán qué números son primos
Se importa la librería sys para correr el programa desde la consola, indicando el input deseado"""
import sys
""" 
Función que crea una lista comenzando del número 1 hasta el número ingresado, 
esto se hace con un contador y regresa la lista
"""
def array (n):
    arr=[]
    i=1
    while i<=n:
        arr.append(i)
        i+=1
    return arr
""" 
Función que toma la lista pasada para crear una nueva con solo los número primos
existentes. Esto se hace con la operación de residuos para así identificar y 
añadir únicamente los números primos, cuando únicamente es divisible entre uno y
si mismo.
"""
def primos (arr):
    primo=[]
    for y in arr:
        z=0
        for x in arr:
            if y%x==0:
                z+=1
        if z==2 or y==1:
            primo.append(y)
    print(primo)
"""
Se introduce el argumento y se corren las funciones
"""
n=int(sys.argv[1])
arr=array(n)
primos(arr)

