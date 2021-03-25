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
url = "http://ligamx.net/cancha/informeArbitral/119522/eyJpZENsdWJsb2NhbCI6MTIwMzcsImlkQ2x1YnZpc2l0YSI6MTEyMjB9/informe-arbitral-gallos-blancos-de-queretaro-vs-club-atletico-de-san-luis-jornada-11-estadio-la-corregidora-imagen-tv--fox-sports"

# Se consigue el código HTML de la pagina
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

# Función para traer infomación de los goles
def marcador_partido():
    
    # Se consigue el resultado e información de los goles a través de la clase marcada
    marcador = soup.findAll("span", {"class": "score"})
    marcador = marcador[0].get_text()
    print("El marcador del partido fue", marcador)
    marcador = marcador.split("-")
    total_goles = int(marcador[0]) + int(marcador[1])
    print("El total de goles fue", total_goles)

def goles_partido():
    gol = soup.findAll("ul", {"class": "row lista-posiciones"})
    print(gol)

marcador_partido()
# goles_partido()