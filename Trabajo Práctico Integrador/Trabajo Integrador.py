import requests
import csv

url = "https://restcountries.com/v3.1/all?fields=name,region,area,population"
data = requests.get(url).json()

with open("paises.csv","w", newline='', encoding="utf-8") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["Nombre", "Población", "Superficie (km²)", "Continente"])
    for country in data:
        nombre = country.get("name", {}).get("common", "")
        poblacion = country.get("population", "")
        area = country.get("area", "")
        continente = country.get("region", "")
        writer.writerow([nombre, poblacion, area, continente])

print("archivo 'paises.csv' creado")