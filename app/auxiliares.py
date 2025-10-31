import csv
from creacion_csv import CSV,PARAMETROS,crear_csv
import os
def normalizar_nombre(nombre:str):
    return nombre.strip().title()


#genera un duplicado en formato lista del csv
def duplicado_csv():
    if not os.path.exists(CSV):
        crear_csv()
    with open(CSV,"r",newline="") as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)

#carga un nuevo csv a partir de una lista
def actualizar_csv(lista:list):
    with open(CSV,"w",newline="") as archivo:
        escritor = csv.DictWriter(archivo,fieldnames=PARAMETROS)
        escritor.writeheader()
        escritor.writerows(lista)

# un contador de paises para mayor visualiazcion, hay casos donde solo un pais es tanto el maximo como el mimino en una lista (filtrar por europa, filtrar entre 0 y 1000 habitantes, el vaticano)
#entonces se añadio el set y su if para evitar contar el pais duplicado
def paises_actuales(lista: list):
    nombres_vistos = set()
    contador_repetidos = 0
    for pais in lista:
        if not isinstance(pais, dict) or "nombre" not in pais:
                # si no cumple, pasar al siguiente elemento
            continue

        nombre = str(pais["nombre"]).strip().lower()

        if nombre in nombres_vistos:
            contador_repetidos += 1
        else:
            nombres_vistos.add(nombre)
    return len(lista) - contador_repetidos

