#################
#**Bibliotecas**#
#################

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
import modulo


#################
#***Funciones***#
#################

def imprimirMenu(menu):
	for i in range(len(menu)):
		print(i+1,'-',menu[i])

def ingreso():
	nombre=input('Ingrese el nombre: ')
	nombre=validar(nombre)
	tel=input('Ingrese el telefono: ')
	tel=validar(tel)
	email=input('Ingrese el e-mail: ')
	email=validar(email)
	email=validarMail(email)
	doc=open('invitados.txt','a')
	string=nombre+','+tel+','+email+'\n'
	doc.write(string)
	doc.close

def lenInvitados():
	documento=open('invitados.txt','r')
	invitados=documento.read()
	invitados=invitados.split('\n')
	return invitados
	
	
def validar(dato):
    while True:
        if dato:
            return dato
        else:
            print('No ingreso nada')
        dato=input('Ingrese de nuevo el dato')

def limpiar():
	os.system('cls')

def validarMail(mail):
        while True:
                if mail.count('@')==1:
                        return mail
                else:
                        print('Ingresaste un mail invalido')
                mail=input('Ingrese de nuevo el mail: ')
          
def enviarMail(mensaje,desde,contraseña,hasta,asunto='Invitados'):
	msg = MIMEMultipart()
	message = mensaje
	password = contraseña
	msg['From'] = desde
	msg['To'] = hasta
	msg['Subject'] = asunto
	msg.attach(MIMEText(message, 'plain'))
	server = smtplib.SMTP('smtp.gmail.com: 587')
	server.starttls()
	server.login(msg['From'], password)
	server.sendmail(msg['From'], msg['To'], msg.as_string())
	server.quit()
	print ("Se ha enviado exitosamente el mail a: %s" % (msg['To']))

	
	
	
################
#*****Main*****#
################

menu=('Ingreso','Ver cantidad de invitados','Salir y enviar')


while True:
	imprimirMenu(menu)
	opc=input()
	limpiar()
	if opc=='1':
		ingreso()
	elif opc=='2':
		invitados=lenInvitados()
		cant=len(invitados)-1
		print(f'Hay {cant} invitados en la sala')
	elif opc=='3':
		invitados=lenInvitados()
		mensaje=''
		for i in range(len(invitados)):
			mensaje+=invitados[i]+'\n'
		enviarMail(mensaje,modulo.mail,modulo.passw,'nicolasgonzalez470@gmail.com')
		break
	else:
		print('Ingresaste una opcion invalida')
	input("Toque ENTER para continuar...")
	limpiar()

	
	
