#######Librerias##############

import requests
import os



########Funciones##############
def imprimir_menu(menu):
	print('Menu: ')
	for i in range(len(menu)):
		print(i+1,'-',menu[i])

def ingresoComensal():
	dato={
	'name':input('Nombre: '),
	'surname':input('Apellido: ')
	}
	r=requests.post('http://127.0.0.1:5000/restaurant',json=dato)
	print("Código de estado:", r.status_code)

def mostrar_comensales():
		r=requests.get('http://127.0.0.1:5000/restaurant')
		datos=r.json()
		for r in datos['restaurant']:
			print(r['id'],r['nombre'],r['apellido'])

def corregir_nombre():
	mostrar_comensales()
	idc=int(input('Ingrese Id del usuario a corregir: '))
	datos={'name':input('Corriga el apellido: ')}
	r=requests.put('http://127.0.0.1:5000/restaurant/'+str(idc),json=datos)
	
def corregir_apellido():
	mostrar_comensales()
	idc=int(input('Ingrese Id del usuario a corregir: '))
	datos={'surname':input('Corriga el nombre: ')}
	r=requests.put('http://127.0.0.1:5000/restaurant/'+str(idc),json=datos)
	
###########Main#################
opciones=['Ingreso','Ver todos los ingresos','Corregir nombre','Corregir apellido','Egreso (Borrar)','Salir']

while True:
	imprimir_menu(opciones)
	opc=input()
	os.system('cls')
	if opc=='1':
		ingresoComensal()
	elif opc=='2':
		mostrar_comensales()
	elif opc=='3':
		corregir_nombre()
	elif opc=='4':
		corregir_apellido()
	elif opc=='5':
		mostrar_comensales()
		numId=input('Ingrese ID del comensal a borrar: ')
		url='http://127.0.0.1:5000/restaurant/'+numId
		r=requests.delete(url)
	elif opc=='6':
		break
	else:
		print('Ingreso una opcion invalida.')
	print()
	print()
	print()
	input('Pulse ENTER para continuar...')
	os.system('cls')
	
