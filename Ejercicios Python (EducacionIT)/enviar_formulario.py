import requests

datos={
	'student':input('Alumno: '),
	'date':input('Fecha (en formato dd/mm/aaaa): '),
	'course':input('Nombre del curso: ')
	
}

r=requests.post('http://localhost:8880/form',data=datos)

if r.status.code==200:
	contenido=r.content.decode('utf-8')
	if 'inscripto' in contenido:
		print('Alumno inscripto correctamente.')
	else:
		print('Te falto agregar campos.')
else:
	print('Hubo un error.')
	
	
