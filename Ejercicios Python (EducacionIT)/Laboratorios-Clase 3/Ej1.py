'''
La función input() solicita al usuario que ingrese un dato a través de la consola y lo
retorna como una cadena. Por ejemplo:
edad = input("Ingresa tu edad: ")
print(edad)
Crear un script que solicite al usuario el código de un país e imprima su nombre, de
acuerdo con el siguiente diccionario:
# Diccionario código: país.
paises = {
"ar": "Argentina",
"es": "España",
"us": "Estados Unidos",
"fr": "Francia"
}
Si el código ingresado no se encuentra en el diccionario, debe imprimir un mensaje en
pantalla y volver a preguntar. Si el usuario escribe “salir”, el programa debe terminar.
'''
paises = {
"ar": "Argentina",
"es": "España",
"us": "Estados Unidos",
"fr": "Francia"
}

while True:
	codigo=input('Ingrese codigo de pais: ')
	if codigo=='salir':
		break
	else:
		try:
			print(paises[codigo])
			break
		except KeyError:
			print('Ingresaste un codigo incorrecto')
		

	

