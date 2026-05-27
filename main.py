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
