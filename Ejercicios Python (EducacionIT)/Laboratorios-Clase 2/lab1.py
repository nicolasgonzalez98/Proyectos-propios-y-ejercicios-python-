'''
En matemática, se conoce a la “sucesión de Fibonacci” como una sucesión infinita de
números naturales en la que cada término está determinado por la suma de los dos
términos anteriores. Por ejemplo, empezando con el 0 y el 1, los primeros 20 términos son
los siguientes:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
1597, 2584, 4181
Crear una función en Python que tome como argumento un entero que indique la cantidad
de términos y retorne una lista como la anterior. Por ejemplo:
>>> fib(10)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
La función debe, además, chequear que el argumento pasado sea mayor a 2. En caso de
ser menor, debe mostrar un mensaje en pantalla y no retornar nada.
>>> fib(1)
La cantidad debe ser mayor a 2.

'''

def fib(n):
    f=[0,1]
    if n>2:
        while len(f)<n:
            num=f[-1]+f[-2]
            f.append(num)
        return f
    else:
        neg='La cantidad debe ser mayor a 2.'
        return neg


num=int(input('Ingrese la cantidad de numeros que desea: '))

print(fib(num))
