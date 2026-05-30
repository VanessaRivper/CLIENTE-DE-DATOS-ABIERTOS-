import requests
import os
import json
import csv
from datetime import datetime

CARPETA = "datos_paises"

if not os.path.exists(CARPETA):
  os.makedirs(CARPETA)

def obtener_datos():
    url = "https://restcountries.com/v3.1/all?fields=name,capital,region,population,area"

    try:
        respuesta = requests.get(url, timeout=20)
        respuesta.raise_for_status()
        return respuesta.json()
    except Exception as e:
        print("Error al obtener datos.", e)
        return []

def guardar_json(datos):

  ruta = os.path.join(CARPETA, "paises.json")

  with open(ruta, "w", encoding="utf-8") as archivo:

    json.dump(datos, archivo, ensure_ascii=False, indent=4)

def limpiar_datos(datos):

  datos_limpios = []

  for pais in datos:

    nombre = pais.get("name", {}).get("common", "No disponible")

    capitales = pais.get("capital", ["No disponible"])
    capital = capitales[0] if capitales else "No disponible"

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

    ruta = os.path.join(CARPETA, "reporte.txt") 

    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write("REPORTE DE DATOS ABIERTOS\n")
        archivo.write(f"Fecha: {datetime.now()}\n")
        archivo.write(f"Total de paises: {total}\n\n")

        archivo.write("Pais mas poblado:\n")
        archivo.write(f"Nombre: {pais_poblado[0]}\n")
        archivo.write(f"Poblacion: {pais_poblado[3]}\n\n")

        archivo.write("Pais con mayor area:\n")
        archivo.write(f"Nombre: {pais_grande[0]}\n")
        archivo.write(f"Area: {pais_grande[4]}\n")
def main(): 
  print("Iniciando programa...")

  datos = obtener_datos()
  if not datos:
    print("No se pudieron obtener datos.")
    return
  
  guardar_json(datos)

  datos_limpios = limpiar_datos(datos)

  guardar_csv(datos_limpios)

  pais_poblado, pais_grande = calcular_estadisticas(datos_limpios)

  crear_reporte(pais_poblado, pais_grande, len(datos_limpios))

  print("Proceso terminado correctamente.")
  print("Archivos generados en la carpeta:", CARPETA)

if __name__ == "__main__":
    main()



