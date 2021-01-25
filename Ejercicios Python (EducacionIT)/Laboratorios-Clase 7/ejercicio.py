########Librerias###############
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

######Funciones#########
def validar(dato):
	while True:
		if dato:
			return dato
		else:
			return messagebox.showinfo(title="Advertencia", message="No ingresaste un nombre.")
		

def saludar():
		global i
		nombre=saludo.get()
		if nombre=='':
			return messagebox.showinfo(title="Advertencia", message="No ingresaste un nombre.")
		if i==5:
			return messagebox.showinfo(title="Advertencia", message="El campo de texto solo permite hasta 5 saludos.")			
		string=f'¡Hola {nombre}!'
		saludo.delete(0,tk.END)
		lista.insert(i,string)
		i+=1

######Main############
i=0

ventana=tk.Tk()
ventana.config(width=300,height=300)
ventana.title('Saludos')

########caja de texto########

saludo=tk.Entry()
saludo.place(x=20,y=10)


####Boton#######

botonSaludo=tk.Button(text='¡Saludar!',command=saludar)
botonSaludo.place(x=150,y=10)

########Lista###########
lista = tk.Listbox()
lista.place(y=60,x=20, width=250)














ventana.mainloop()
