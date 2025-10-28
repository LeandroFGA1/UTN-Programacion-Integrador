import requests

paises = "paises.csv"


def traduccion_continente(nombre:str):
    if nombre == "Americas":
        return "América"
    if nombre == "Europe":
        return "Europa"
    if nombre == "Africa":
        return "África"
    return nombre

def crear_csv(data_paises):
    if data_paises != False:
        bandera:bool = True
    else:
        bandera:bool = False
    
    if bandera:
        with open(paises,"w") as archivo:
            for pais in data_paises :
                nombre = str(pais["translations"]["spa"]["common"]).title().replace(",","-")
                poblacion = int(pais["population"])
                superficie = int(pais["area"])
                continente = traduccion_continente(str(pais["region"]).title())
                if not continente == "Antarctic": #no existen paises antarticos, hay paises en la antartida del tratado antartico pero ninguna tiene una soberania real fuera de sus bases. Por eso se desicidio no incluir los que tengan esto
                    archivo.write(f"{nombre},{poblacion},{superficie},{continente} \n")
    else:
        with open("paises_reserva.csv","r") as archivo:
            with open(paises,"a") as archivo_nuevo:
                for pais in archivo:
                    linea = pais.strip().split(",")#[0]nombre,[1]poblacion,[2]superficie,[3]continente
                    linea[3] = traduccion_continente(linea[3])
                    if not linea[3] == "Antarctic": #no hay paises en la antartida
                        archivo_nuevo.write(f"{linea[0]},{linea[1]},{linea[2]},{linea[3]}")

def descargar_csv():
    url = "https://restcountries.com/v3.1/all?fields=translations,region,area,population,independent"
    try:
        data_paises = requests.get(url).json()
        return data_paises
    except: 
        print("error")
        data_paises = False
        return data_paises
    
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



def filtro_continente(continente:str):
    lista_continente =[]
    with open(paises,"r") as archivo:
        for pais in archivo:
            linea = pais.strip().split(",")
            if linea[3] == continente:
                lista_continente.append([linea[0],linea[1],linea[2]])
    return lista_continente


def filtro_rango_poblacion_superficie(minimo:int,maximo:int,tipo:int):
    if minimo == maximo or minimo > maximo:
        return f"entrada invalida"
    lista_rango_poblacion_superficie = []
    with open(paises,"r") as archivo:
        for pais in archivo:
            linea = pais.strip().split(",")
            if minimo <= int(linea[tipo]) <= maximo:
                lista_rango_poblacion_superficie.append([linea[0],linea[1],linea[2],linea[3]])
        if lista_rango_poblacion_superficie == []:
            return "no existe pais que cumpla esos parametros"
        return lista_rango_poblacion_superficie


def filtrar_paises(filtro:str):
    filtro = filtro.strip().lower()
    if filtro == "1": #continentes
        print(filtro_continente("Oceania"))
    elif filtro == "2": #rango de poblacion a-b incluidos
        print(filtro_rango_poblacion_superficie(1000,2001,1))
    elif filtro == "3": #rango de superficie a-b incluidos
        print(filtro_rango_poblacion_superficie(1000,2001,2))
    else:
        print("invalido")


def nombre_pais(pais):
    return pais[0]

def ordenar_paises_az(orden:str):
    orden = orden.strip().lower()
    lista_ordenada = []
    with open(paises,"r") as archivo:
        for pais in archivo:
            linea = pais.strip().split(",")
            lista_ordenada.append(linea)
    
    if orden == "a":
        lista_ordenada.sort(key=nombre_pais)

    elif orden =="z":
        lista_ordenada.sort(key=nombre_pais, reverse=True)
    else:
        return "error"
    return lista_ordenada



def ordenar_paises(ordenar:str):
    ordenar = ordenar.strip().lower()
    if ordenar =="1": #nombre A-Z o Z-A
        return ordenar_paises_az("z")
    elif ordenar =="2": #poblacion -> de mayor a menor o de menor a mayor
        print()
    elif ordenar =="3": #superficie -> de mayor a menor o de menor a mayor
        print()
    else:
        print("invalido")

def mostrar_estadistica(mostrar:str):
    mostrar = mostrar.strip.lower()
    if mostrar =="1": # el pais con mayor poblacion y el menor
        print()
    elif mostrar =="2": # promedio de poblacion -- no entendi
        print()
    elif mostrar =="3": # promedio de superficie -- no entendi
        print()
    elif mostrar =="4": #cantidad de paises por continente
        print()
    else:
        print("invalido")

def main(): #harcodeado para pruebas , no version final
    crear_csv(descargar_csv())
    buscado = busqueda_exacta_parcial("chi")
    if len(buscado) >= 1:
        print("no se encontro dicho pais, pero puede que haya querido menciona uno de los siguientes?")
    for i in range(len(buscado)):
        print(buscado[i])
    filtrar_paises("3")
    print("hola \n")
    print(ordenar_paises("1"))

main()