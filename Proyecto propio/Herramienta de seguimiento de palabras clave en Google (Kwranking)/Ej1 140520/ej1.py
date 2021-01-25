#######Librerias###########

import os
import requests
from bs4 import BeautifulSoup
import lxml

#######Funciones###########

def imprimirMenu():
	print('-----')
	print('-----')
	print('KwRanking')
	print()
	print('[1] – Importar palabras clave')
	print('[2] – Mostrar palabras clave')
	print('[3] - Comprobar palabras clave')
	print('[0] – Salir')

def limpiar():
	os.system('cls')
	
def carga_keywords():
	keywords=[]
	documento=open('keywords.txt')
	for lineas in documento:
		lineas=lineas.strip()
		keywords.append(lineas)
	return keywords

def mostrarKeywords(lista):
	contador=0
	for comida in lista:
		print(comida)
		contador+=1
		if contador==20:
			contador=0
			input('Pulse ENTER para seguir...')			
	
def comprueba_keywords(kw, dominio):
	clase="TbwUpd NJjxre"
	direcc=[]
	for start in range(0,100,10):
		url=f'https://www.google.com/search?q={kw}&start={start}'
		r=requests.get(url)
		soup = BeautifulSoup(r.text, 'lxml')
		
		
		
		
	
#########Main##############
kw='python'
dominio='python.org'

while True:
	imprimirMenu()
	opc=input()
	limpiar()
	if opc=='0':
		print('Muchas gracias por usar la aplicacion.')
		break
	elif opc=='1':
		keywords=carga_keywords()
	elif opc=='2':
		mostrarKeywords(keywords)
	elif opc=='3':
		enlaces=comprueba_keywords(kw, dominio)
		print(enlaces)
	else:
		print('Ingresaste una opcion invalida')
	input('Pulse ENTER para continuar...')
	limpiar()
		

