siwhile True:
    a=input('Ingrese el primer numero: ')
    b=input('Ingrese el otro numero: ')
    try:
        a=int(a)
        b=int(b)
        print('a+b: ',a+b)
        print('a-b: ',a-b)
        print('a*b: ',a*b)
        print('a/b: ',a/b)
        break
    except ZeroDivisionError:
        print('No se puede dividir por cero.')
    except ValueError:
        print('No ingresaste un dato valido.')
        
