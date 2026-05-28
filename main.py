import requests
import os
import json
import csv
from datetime import datetime

CARPETA = "datos_paises"

if not os.path.exists(CARPETA):
  os.makedirs(CARPETA)

def obtener_datos():

  url =

  try: 

      respuesta = respuesta.get(
        url,
        timeout=10
      )

      respuesta.raise_for_status()

      return respuesta.json()

  except Exception:
    print("Error al obtener datos.")
    return []

def guardar_json(datos):

  ruta = os.path.join(CARPETA, "paises.json")

  with open(ruta, "w", encoding="utf-8") as archivo:

    json.dump(datos, archivo, ensure_ascii=False, indent=4)

def limpiar_datos(datos):

  datos_limpios = []

  for pais in datos:

    nombre = pais.get("name", {}).get("common", "No disponible")

    capital = (pais.get("capital", ["No disponible"])[0])

    region = pais.get("region", "No disponible")

    poblacion = pais.get("population", 0)

    area = pais.get("area", 0)

    datos_limpios.append([nombre, capital, region, poblacion, area])

return datos_limpios
