import pandas as pd 
import googlemaps
import os

#Cambiar working directory

os.chdir("/Users/iriqu/Desktop/Gonzalo")

#Obtener working directory

os.getcwd()
#, usecols=['Dirección'], index_col=['Dirección']
df = pd.read_csv("proyectosinmobrm.csv", encoding='latin-1', header=0, sep=";")

# para tomar todas las filas y la columna 1


gmaps_key = googlemaps.Client(key = "AIzaSyCGQxf8vH33vc-voXDmEYIhdo3IPIqOs_g")

df["LAT"] = None
df["LON"] = None

#df.iat[x,y] tal como una matriz

for i in range(0, len(df), 1):
	geocode_result = gmaps_key.geocode(df.iat[i,1])
	try:
		lat = geocode_result[0]['geometry']['location']['lat']
		lon = geocode_result[0]['geometry']['location']['lng']
		df.iat[i, df.columns.get_loc("LAT")] = lat
		df.iat[i, df.columns.get_loc("LON")] = lon
	except:
		lat = None
		lon = None	

df.to_csv("geocoderm.csv")
