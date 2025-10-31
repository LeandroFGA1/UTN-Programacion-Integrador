import requests
import os
import csv

BASE_DIRECTORIO = os.path.dirname(__file__)
CSV = os.path.join(BASE_DIRECTORIO,"paises.csv") 
CSV_RESPALDO =os.path.join(BASE_DIRECTORIO,"paises_reserva.csv") #el respaldo es un csv que se creo y se renombro durante el desarrollo del TPI
PARAMETROS = ["nombre","poblacion","superficie","continente","independencia"]


def traduccion_continente(nombre:str):
    if nombre == "Americas":
        return "América"
    if nombre == "Europe":
        return "Europa"
    if nombre == "Africa":
        return "África"
    if nombre =="Oceania":
        return "Oceanía"
    return nombre # los demas continentes se escriben igual que en ingles


def descargar_csv():
    url = "https://restcountries.com/v3.1/all?fields=translations,region,area,population,independent"
    try:
        data_paises = requests.get(url).json()
        return data_paises
    except: #un respaldo local por si por la razon que fuera, la api no funciona
        print("error")
        data_paises = False
        return data_paises


def crear_csv():
    if os.path.exists(CSV): #por si ya existe el archivo
        print("archivo ya existente")
        return
    paises = descargar_csv()
    
    if paises == False: #por si no se logro descargar, se hace una copia de la reserva
        with open(CSV_RESPALDO,"r",newline="",encoding="utf-8") as archivo:
            lector =csv.DictReader(archivo)
            lector = list(lector)   
    else: #si se logro descargar con exito
        lector = []
        for pais in paises:
            nombre = str(pais["translations"]["spa"]["common"]).title().replace(",","-") #hay algunos paises con , en el nombre, esto previene errores
            poblacion = (pais["population"])
            superficie = (pais["area"])
            if superficie == int(superficie):
                superficie = int(superficie)
            continente = traduccion_continente(str(pais["region"]).title())
            independencia = bool(pais["independent"])
            if continente !="Antarctic":
                lector.append({
                    "nombre":       nombre,
                    "poblacion":    poblacion,
                    "superficie":   superficie,
                    "continente":   continente,
                    "independencia":independencia
                })
    with open(CSV,"w",newline="",encoding="utf-8") as archivo: #creacion como tal del archivo
            escritor = csv.DictWriter(archivo,fieldnames=PARAMETROS)
            escritor.writeheader()
            escritor.writerows(lector)