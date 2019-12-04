from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
my_url = 'https://www.portalinmobiliario.com/venta/departamento/vitacura-metropolitana?ca=3&ts=1&mn=2&or=&sf=1&sp=0&at=0&pg=1'

#conectandome a la web, tomando la página
uClient = uReq(my_url)
page_html = uClient.read() 
uClient.close()

#html parser
page_soup = soup(page_html, "html.parser")

#toma cada product
containers = page_soup.findAll('div',{'class':'row product-item proyecto destacada pagada'})

filename = "propiedades.csv"
f = open(filename, "w")

headers = "Dirección, Precio, Superficie\n"

f.write(headers)

for container in containers:

	direccion_container = container.findAll('div',{'class':'col-sm-6 product-item-summary'})
	sub_container = direccion_container[0].findAll('p')
	direccion = sub_container[1].text

	datos_container = container.findAll('div',{'class':'col-sm-3'})
	precio = datos_container[1].span.text
	superficie = datos_container[2].span.text

	print ("Dirección: " + direccion)
	print ("Precio: " + precio)
	print ("Superficie: " + superficie)

	f.write(direccion.replace(",",".") + "," + precio.replace(",",".") + "," + superficie.replace(",",".") + "\n")

f.close()
