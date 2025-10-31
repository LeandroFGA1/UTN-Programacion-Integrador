import csv
from creacion_csv import CSV,PARAMETROS,crear_csv
import os
def normalizar_nombre(nombre:str):
    return nombre.strip().title()



def duplicado_csv():
    if not os.path.exists(CSV):
        crear_csv()
    with open(CSV,"r",newline="") as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)


def actualizar_csv(lista:list):
    with open(CSV,"w",newline="") as archivo:
        escritor = csv.DictWriter(archivo,fieldnames=PARAMETROS)
        escritor.writeheader()
        escritor.writerows(lista)