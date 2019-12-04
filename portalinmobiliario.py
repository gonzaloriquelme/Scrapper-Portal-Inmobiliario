from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
my_url = 'https://www.portalinmobiliario.com/venta/departamento/vitacura-metropolitana?tp=2&op=1&ca=1&ts=1&dd=0&dh=6&bd=0&bh=6&or=&mn=2&sf=1&sp=0&pi=uoxk3dm1qjrmqn4igorf05fl'

#conectandome a la web, tomando la página
uClient = uReq(my_url)
page_html = uClient.read() 
uClient.close()

#html parser
page_soup = soup(page_html, "html.parser")

#toma cada product
paginas = round(int(page_soup.findAll('div',{'class':'pagination-right'})[0].span.text[20:])/25)

my_url = 'https://www.portalinmobiliario.com/venta/departamento/vitacura-metropolitana?ca=1&ts=1&mn=2&or=&sf=1&sp=0&at=0&pg='

filename = "proyectosinmob.csv"
f = open(filename, "w")

headers = "Comuna, Dirección, Precio, Superficie, Fecha de entrega, Propietario, Construye, Arquitectos, Vende  \n"

f.write(headers)

for i in range(1,paginas+1):
	my_url ='https://www.portalinmobiliario.com/venta/departamento/vitacura-metropolitana?ca=1&ts=1&mn=2&or=&sf=1&sp=0&at=0&pg='+str(i)
	print(my_url)
	uClient = uReq(my_url)
	page_html = uClient.read() 
	uClient.close()
	page_soup = soup(page_html, "html.parser")
	containers = page_soup.findAll('div',{'class':['row product-item proyecto destacada pagada','row product-item proyecto pagada']})

	for container in containers:

		direccion_container = container.findAll('div',{'class':'col-sm-6 product-item-summary'})
		sub_container = direccion_container[0].findAll('p')
		direccion = sub_container[1].text
		my_urldos = 'https://www.portalinmobiliario.com' + direccion_container[0].h4.a['href']
		uClient = uReq(my_urldos)
		page_htmldos = uClient.read()
		uClient.close()
		page_soupdos = soup(page_htmldos, "html.parser")
		otra_info = page_soupdos.findAll('div',{'class':'prj-other-info-item'})
		otros =""
		datos_container = container.findAll('div',{'class':'col-sm-3'})
		precio = datos_container[1].span.text
		superficie = datos_container[2].span.text
		compara = ["Fecha de entrega","Propietario","Construye","Arquitectos","Vende"]
		vec = [' ',' ',' ',' ',' ']
		otros = ""
		for item in otra_info:
			vec[compara.index(item.strong.text)] = item.text
		otros= otros + vec[0][17:].replace(",","|") + ","
		otros= otros + vec[1][12:].replace(",","|") + ","
		otros= otros + vec[2][10:].replace(",","|") + ","
		otros= otros + vec[3][12:].replace(",","|") + ","
		otros= otros + vec[4][6:].replace(",","|") + ","
		comuna = direccion.rsplit(",",1)[-1][1:]
		print (otros)
		print ("Dirección: " + direccion)
		print ("Precio: " + precio)
		print ("Superficie: " + superficie)

		f.write(comuna + "," + direccion.replace(",",".") + "," + precio.replace(",",".") + "," + superficie.replace(",",".") +","+ otros+ "\n")

f.close()
