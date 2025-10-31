import os
from creacion_csv import crear_csv,BASE_DIRECTORIO,CSV,PARAMETROS
from auxiliares import normalizar_nombre,duplicado_csv,actualizar_csv
import csv


def buscar_pais(nombre:str):
    if not nombre.strip().replace(" ","").replace(",","").isalpha():
        return {"error":"entrada invalida"}
    if len(nombre.replace(" ","")) < 3:
        return {"error":"coloque al menos 3 letras"}
    nombre = normalizar_nombre(nombre)
    with open(CSV,"r",newline="",encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        paises = list(lector)
        paises_parcial = []
        for pais in paises:
            if pais["nombre"] == nombre.replace(" ","-"):
                return pais
            elif nombre.replace(" ","-") in pais["nombre"]:
                paises_parcial.append(pais)
        if paises_parcial == []:
            return {"error":f"no se encontro el pais ni un aproximado a {nombre}"}
        else:
            return paises_parcial

def filtrar_continentes(continente:str):
    lista = duplicado_csv()
    lista_filtrada=[]
    for pais in lista:
        if pais["continente"] == continente:
            lista_filtrada.append(pais)
    if lista_filtrada == []:
        return {"error":"continente inexistente o fuera del resgistro actual"}
    else:
        actualizar_csv(lista_filtrada)
        return lista_filtrada


def filtrar_rango(minimo: int, maximo: int, tipo: str):
    if minimo >= maximo:
        return {"error": "entrada invalida, el mínimo debe ser menor al máximo"}

    lista = duplicado_csv()
    lista_filtrada = []

    for pais in lista:
        valor_str = str(pais[tipo]).strip().replace(",", ".") 
        if valor_str == "":
            continue
        if "." in valor_str:
            valor_str = valor_str.split(".")[0]
        if not valor_str.isdigit():
            continue
        valor = int(valor_str)
        if minimo <= valor <= maximo:
            lista_filtrada.append(pais)
    if not lista_filtrada:
        return {"error": f"No hay países con {tipo} entre {minimo} y {maximo}"}
    actualizar_csv(lista_filtrada)
    return lista_filtrada



def ordenar_paises_por_nombre(criterio: str):
    lista_datos = duplicado_csv() 
    if criterio == "nombre_az":
        ascendente = True
    elif criterio == "nombre_za":
        ascendente = False
    else:
        return {"error": "criterio invalido"}
    lista_nombres = []
    for pais in lista_datos:
        lista_nombres.append(pais["nombre"])
    nombres_ordenados = sorted(lista_nombres, reverse=not ascendente)
    lista_ordenada = []
    for nombre in nombres_ordenados:
        for pais in lista_datos:
            if pais["nombre"] == nombre:
                lista_ordenada.append(pais)
    actualizar_csv(lista_ordenada)
    return lista_ordenada

def ordenar_paises_por_numero(criterio: str, clave: str):
    lista_datos = duplicado_csv()

    # Verificar el criterio
    if criterio == f"{clave}_menos":
        ascendente = True
    elif criterio == f"{clave}_mas":
        ascendente = False
    else:
        return {"error": "criterio invalido"}
    for for_externo in range(len(lista_datos)):
        for for_interno in range(for_externo + 1, len(lista_datos)):
            a_str = str(lista_datos[for_externo][clave]).strip().replace(",", ".")
            b_str = str(lista_datos[for_interno][clave]).strip().replace(",", ".")

            # Si tienen punto, tomar solo la parte entera
            if "." in a_str:
                a_str = a_str.split(".")[0]
            if "." in b_str:
                b_str = b_str.split(".")[0]

            # Validar que sean numéricos
            if not a_str.isdigit() or not b_str.isdigit():
                continue
            a = int(a_str)
            b = int(b_str)

            if ascendente and a > b:
                lista_datos[for_externo], lista_datos[for_interno] = lista_datos[for_interno], lista_datos[for_externo]
            elif not ascendente and a < b:
                lista_datos[for_externo], lista_datos[for_interno] = lista_datos[for_interno], lista_datos[for_externo]
    actualizar_csv(lista_datos)
    return lista_datos


def ordenar_paises(criterio: str):
    if criterio in ["nombre_az", "nombre_za"]:
        return ordenar_paises_por_nombre(criterio)
    elif criterio in ["poblacion_mas", "poblacion_menos"]:
        return ordenar_paises_por_numero(criterio, "poblacion")
    elif criterio in ["superficie_mas", "superficie_menos"]:
        return ordenar_paises_por_numero(criterio, "superficie")
    else:
        return {"error": "criterio invalido"}

def min_max_poblacion():
    datos_ordenados = ordenar_paises_por_numero("poblacion_mas","poblacion")
    min_dato = datos_ordenados[0]
    max_dato = datos_ordenados[-1]
    minimos_datos = []
    minimos_datos.append(min_dato)
    maximos_datos = []
    maximos_datos.append(max_dato)
    len_datos = len(datos_ordenados)
    for i in range(1, len_datos):
        dato_actual = datos_ordenados[i]
        if dato_actual["poblacion"] == min_dato["poblacion"]:
            minimos_datos.append(dato_actual)
        else:
            break
    for j in range(len_datos - 2, -1, -1):
        dato_actual = datos_ordenados[j]
        if dato_actual["poblacion"] == max_dato["poblacion"]:
            maximos_datos.append(dato_actual)
        else:
            break
    for pais in minimos_datos:
        pais["nombre"] = f"{pais['nombre']} (menor gente)"
    for pais in maximos_datos:
        pais["nombre"] = f"{pais['nombre']} (mayor gente)"
    return minimos_datos + maximos_datos


def promedio_poblacion():
    datos = duplicado_csv()
    suma_poblacion = 0
    valores = []
    for pais in datos:
        valores.append(pais["poblacion"])
    #obtenemos la cantidad de valores
    total_paises = len(valores)
    #iteramos por la lista de valores y sumamos
    for valor in valores:
        #sumamos el valor a la suma total
        suma_poblacion += int(valor)
    #ya con la suma total y la cantidad de valores, calculamos el promedio con la cifras decimales deseadas
    promedio = round(suma_poblacion / total_paises, 0)
    print(f" el promedio de la poblacion por pais, considerando que la poblacion total es {suma_poblacion} y la cantidad de paises es de {total_paises} es de: {promedio}")
    return {"promedio de poblacion por pais":int(promedio)}


def promedio_superficie():
    datos = duplicado_csv()
    suma_superficie = 0
    valores = []
    for pais in datos:
        valores.append(pais["superficie"])
    total_paises = len(valores)

    for valor in valores:
        suma_superficie += float(valor)

    promedio = round(suma_superficie / total_paises, 0)

    return {"promedio de superficie por pais": int(promedio)}


def paises_por_continente():
    datos = duplicado_csv()
    continentes = ["África", "América", "Asia", "Europa", "Oceanía"]

    lista_resultado = []

    for cont in continentes:
        cantidad = 0
        for pais in datos:
            if pais["continente"] == cont:
                cantidad += 1
        lista_resultado.append({"continente": cont, "cantidad": cantidad})

    return lista_resultado
