import subprocess
import os
import sys

arg=sys.argv

try:
    process=arg[1]
except IndexError:
    print('No has introducido los argumentos necesarios.')
    sys.exit()



p=subprocess.run('C:/Users/Nico/Desktop/Carrera Python/Python programming/Ejercicios Python (EducacionIT)/Laboratorios-Clase 5/processinfo.exe',  capture_output=True, encoding="cp850")
p=p.stdout
t=p.find('0')
lista=p[t:].split('|')

for i in range(len(lista)):
    lista[i]=lista[i].strip()

i=0
procesos=[]

while i<len(lista):
    procesos.append((lista[i],lista[i+1],lista[i+2]))
    i+=4

for i in range(len(procesos)):
    if procesos[i][1].startswith(process):
        print('PID: ',procesos[i][0],'Usuario: ',procesos[i][2])
