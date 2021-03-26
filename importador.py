""" Aqui se coloca todo lo que hace el modulo a que contexto el corresponde """

__author__ = "Carlos Alberto Montes Romero"
__copyright__ = "Copyright 2021, UTNG"
__credits__ = "Estadisticas Fut"

__licence__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Carlos Montes"
__email__ = "carloss.montes@gmail.com"
__status__ = "Development"

import csv
import requests
import smtplib
from bs4 import BeautifulSoup
from datetime import datetime

# Necesario para conseguir información de la pagina. Buscar por User-Agent
headers = {"User-Agent":  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36 OPR/74.0.3911.232'}

# URL del partido
url = "http://ligamx.net/cancha/informeArbitral/119524/eyJpZENsdWJsb2NhbCI6OSwiaWRDbHVidmlzaXRhIjoyOX0=/informe-arbitral-leon-vs-necaxa-jornada-11-estadio-nou-camp-fox--claro-sports"

# Se consigue el código HTML de la pagina
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

# Se consigue el resultado e información de los goles a través de la clase marcada
marcador = soup.findAll("span", {"class": "score"})
marcador = marcador[0].get_text()
marcador_final = marcador
# Variable para poder conocer los anotadores y minutos del gol
marcador = marcador.split("-")
total_goles = int(marcador[0]) + int(marcador[1])

# Se encuentra informacion de fecha, hora, anotadores
anotador = soup.findAll("div", {"class": "col-xs-6"})

def fecha():
    # Se imprime la informacion dando formato al texto
    print("El partido se jugó el", anotador[0].get_text().lstrip('\n').rstrip('\n'), "a las", anotador[1].get_text().lstrip('\n'))

# Función para traer infomación de los goles
def marcador_partido():
    # Se imprime informacion del marcador
    print("El marcador del partido terminó", marcador_final)
    print("El total de goles fue", total_goles, "\n")

# Función para dar a conocer los anotadores y minutos del gol
def goles_partido():
    # Etiquetas donde se encuentra información
    min_gol = soup.findAll("div", {"class": "col-xs-2 minutoGol"})

    # Ciclo para recorrer la información obtenida de anotador y minuto del gol
    for i in range(total_goles):
        # Información encontrada en los primeros elementos
        minuto = min_gol[i].get_text()
        minuto = minuto.split("n")

        # Informacion encontrada en los primeros + 2 elementos
        anota = None
        anota = anotador[i + 2].get_text()
        anota = anota.lstrip().rstrip()
        anota = anota.split("#")

        # Se imprime la información encontrada
        print("Gol de", anota[0].rstrip('\n') , "al", minuto[0] + "n", minuto[1])
    
    print("\n")

fecha()
marcador_partido()
goles_partido()