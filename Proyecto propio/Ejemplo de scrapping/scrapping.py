from urllib.request import urlopen

pagina=urlopen('https://www.cuspide.com/cienmasvendidos/')

html=pagina.read().decode('utf8')

libros=[]

for num in range(0,10):
	pos=html.find('ctl0'+str(num)+'_img_tapa')
	segmento=html[pos+58:pos+150]
	posf=segmento.find('"')
	nombreLibro=segmento[:posf]
	libros.append(nombreLibro)

for num in range(10,89):
	pos=html.find('ctl'+str(num)+'_img_tapa')
	segmento=html[pos+58:pos+150]
	posf=segmento.find('"')
	nombreLibro2=segmento[:posf]
	libros.append(nombreLibro2)
	print(nombreLibro2)
