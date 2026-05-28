import requests
import os
import json
import csv
from datetime import datetime

CARPETA = "datos_paises"

if not os.path.exists(CARPETA):
  os.makedirs(CARPETA)

def obtener_datos():

  url =  https://restcountries.com/v3.1/all?fields=name,capital,region,population,area,flags,languages,
currencies,timezones,borders


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

def guardar_csv(datos):

  ruta = os.path.join(CARPETA, "paises.csv")

  with open(ruta, "w", newline="", encoding="utf-8") as archivo:

      escritor = csv.writer(archivo)

      escritor.writerow(["Nombre", "Capital", "Region", "Población", "Area"])

      escritor.writerows(datos)

def calcular_estadisticas(datos):

  pais_poblado = max(datos, key=lambda x:[3])

  pais_grande = max(datos, key=lambda x: x[4])

  return (pais_poblado, pais_grande)

def crear_reporte(pais_poblado, pais_grande, total):

  print("Iniciando programa...")

  datos = obtener_datos()
