######Librerias######
import sqlite3

#####Funciones#######

#####Main############

conn=sqlite3.connect('productosdb.sqlite')
cursor=conn.cursor()

#Crear tabla

#table='CREATE TABLE productos (id INT,nombre TEXT,precio INT)'
#cursor.execute(table)

#Agregar Datos

#productos=[(1,'Teclado',500),(2,'Mouse',350),(3,'Monitor',1500),(4,'Parlantes',1100)]


#for idNum,nombre,precio in productos:
#	cursor.execute('INSERT INTO productos VALUES (?,?,?)',(idNum,nombre,precio))
	
#Ejercicio 2

cursor.execute('SELECT id FROM productos')
datos=cursor.fetchall()
ids=[]

for i in range(len(datos)):
	ids.append(datos[i][0])

agregarDato='INSERT INTO productos VALUES (?,?,?)'

while True:
	print('1-Ingresar dato')
	print('2-Salir')
	opc=input()
	if opc=='1':
		idNum=int(input('Ingrese ID del producto: '))
		while idNum in ids:
			print('Ese articulo ya existe, ingrese otro.')
			idNum=int(input('Ingrese iD del producto: '))	
		ids.append(idNum)
		nombre=input('Ingrese nombre del producto: ')
		precio=int(input('Ingrese precio: '))
		cursor.execute(agregarDato,(idNum,nombre,precio))
		print('Se cargo todo perfectamente.')
	elif opc=='2':
		print('Gracias por usar la app')
		break
	else:
		print('Ingreso un dato erroneo')
	
	










conn.commit()

conn.close()

