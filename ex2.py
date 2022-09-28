#Ejercicio de arreglo de 1 hasta n números, se identificarán qué números son primos
import sys
def array (n):
    arr=[]
    i=1
    while i<=n:
        arr.append(i)
        i+=
        #comentario
    return arr
def primos (arr):
    primal=[]
    y=1
    for x in arr:
        if x/y==1:
            y+=1
            primal.append(y)
            for z in primal:
                if z!=1 && z!=y && kind(y/z)==int:
                    primal.delete(z)
    return primal
n=sys.argv[1]
n=int(n)
arr=array(n)
print(arr)
print(primos(arr))

