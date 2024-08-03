import requests
from Pelicula import Pelicula
from Especie import Especie
from Personaje import Personaje

def start():
    None

class StarWar:
    datos_obj=[]
    pelicula_obj=[]
    especie_obj=[]
    personaje_obj=[]

    def leer_datos():
        url="https://www.swapi.tech/api/"
        data = requests.get(url)
        if data.status_code == 200:
            data = data.json()
        return data
    

