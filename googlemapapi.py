import urllib.request
import json

endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyCyTbu3yhFqvaxs9PXq_kA54OmDT67ew0w'

#origen = input('Where are you?: ').replace(" ","+")
origen="santiago"
destino="talca"
#destino = input('Where do you want to go?: ').replace(" ","+")

nav_request = 'origin={}&destination={}&key={}'.format(origen,destino,api_key)

print(nav_request)

request = endpoint + nav_request
response = urllib.request.urlopen(request).read()


directions = json.loads(response)

routes = directions['routes']

legs = routes[0]['legs']

distancia = legs[0]['distance']['text']

print(distancia)