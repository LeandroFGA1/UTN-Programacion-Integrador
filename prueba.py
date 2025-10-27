import requests

paises = "paises.csv"
paises_dependientes_y_otros={}


def traduccion_continente(nombre:str):
    if nombre == "Americas":
        return "America"
    if nombre == "Europe":
        return "Europa"
    return nombre


def descargar_creacion_csv():
    url = "https://restcountries.com/v3.1/all?fields=translations,region,area,population,independent"
    bandera:bool = True
    try:
        data_paises = requests.get(url).json()
    except: 
        print("error")
        bandera = False

    if bandera:
        with open(paises,"w") as archivo:
            for pais in data_paises:
                nombre = str(pais["translations"]["spa"]["common"]).title()
                poblacion = int(pais["population"])
                superficie = int(pais["area"])
                continente = traduccion_continente(str(pais["region"]).title())
                independencia =bool(pais["independent"])

                if not independencia:
                    paises_dependientes_y_otros[nombre] = False
                if not continente == "Antarctic": #no existen paises antarticos, hay paises en la antartida del tratado antartico pero ninguna tiene una soberania real fuera de sus bases. Por eso se desicidio no incluir los que tengan esto
                    archivo.write(f"{nombre},{poblacion},{superficie},{continente} \n")
    else:
        with open("paises_reserva.csv","r") as archivo:
            with open(paises,"a") as archivo_nuevo:
                for pais in archivo:
                    linea = pais.strip().split(",")#[0]nombre,[1]poblacion,[2]superficie,[3]continente,[4]independencia
                    if not linea[4]:
                        paises_dependientes_y_otros[linea[0]] = False
                    linea[3] = traduccion_continente(linea[3])
                    if not linea[3] == "Antarctic":
                        archivo_nuevo.write(f"{linea[0]},{linea[1]},{linea[2]},{linea[3]}")

def busqueda_exacta_parcial(nombre:str):
    nombre = nombre.strip().title()
    if len(nombre) <3 or not nombre.isalpha(): #la investigacion dio que no hay paises con nombres menores a 4 caracteres
        print("nombre muy corto y/o no son caracteres")
        return f"entrada invalida"
    with open(paises,"r") as archivo:
        aproximados = []
        for pais in archivo:
            pais_actual = pais.strip().split(",")
            #en las siguientes lineas pense que me repetia innecesariamente pero si creo una variable con el contenido antes de los condicionales eso haria mas ineficiente el bucle por que crearia uno por pais.
            if nombre == pais_actual[0]:
                return [f"el pais {pais_actual[0]} tiene una poblacion de: {pais_actual[1]}, una superficie en kilometros cuadrados de: {pais_actual[2]} y esta ubicado en el continente de {pais_actual[3]}"]
            elif nombre in pais_actual[0]:
                aproximados.append(f"el pais {pais_actual[0]} tiene una poblacion de: {pais_actual[1]}, una superficie en kilometros cuadrados de: {pais_actual[2]} y esta ubicado en el continente de {pais_actual[3]}")
        if aproximados == []:
            return [f"no existe dicho pais"]
        else:
            return aproximados                

def filtrar_paises(filtro:str):
    filtro = filtro.strip().lower()
    if filtro == "1": #continentes
        print("")
    elif filtro == "2": #rango de poblacion
        print("")
    elif filtro == "3": #rango de superficie
        print("")



def main():                        
    descargar_creacion_csv()
    print(paises_dependientes_y_otros)
    buscado = busqueda_exacta_parcial("chi")
    if len(buscado) >= 1:
        print("no se encontro dicho pais, pero puede que haya querido menciona uno de los siguientes?")
    for i in range(len(buscado)):
        print(buscado[i])


main()