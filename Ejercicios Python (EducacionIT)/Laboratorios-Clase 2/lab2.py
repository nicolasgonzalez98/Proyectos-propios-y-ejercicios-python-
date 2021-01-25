'''
Escribir una función que, dado un número máximo, retorne una lista con todos los números
desde 1 hasta dicho número que sean simultáneamente múltiplos de 3 y de 5 (usar la
operación resto con el carácter %).
>>> multiplos(100)
[15, 30, 45, 60, 75, 90]
'''
def multiplos(n):
    mult=[]
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            mult.append(i)
    return mult



