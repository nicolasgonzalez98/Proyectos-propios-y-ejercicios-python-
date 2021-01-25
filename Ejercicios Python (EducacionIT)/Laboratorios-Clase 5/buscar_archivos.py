####Librerias######

import os
import sys


###Main###
lista=sys.argv

try:
	direcc=lista[1]
	ext=lista[2]
except IndexError:
	print('Argumentos insuficientes. Indique la ruta en donde buscar y la extensión.')
	sys.exit()
	
try:
	archivos=os.listdir(direcc)
except FileNotFoundError:
	print('La ruta '+direcc+' no existe.')
	sys.exit()

if ext.startswith('.')==False:
	ext='.'+ext

print('Archivos con extención '+ext)

for n in archivos:
	if n.endswith(ext):
		print(n)


