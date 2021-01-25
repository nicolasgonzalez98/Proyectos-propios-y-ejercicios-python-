import sqlite3

conn=sqlite3.connect('productosdb.sqlite')
cursor=conn.cursor()

cursor.execute('SELECT id FROM productos')
datos=cursor.fetchall()
idNum=[]

for i in range(len(datos)):
	idNum.append(datos[i][0])
	
print(idNum)
	
