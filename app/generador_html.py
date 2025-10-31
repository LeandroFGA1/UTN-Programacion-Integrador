def generar_html_salidas(datos):
    # genera una salida en formato html de los datos manipulados previamentente, distiguiendo entre las posibles salidas.

    #si es un str, lo sube tal cual
    if isinstance(datos, str):
        return f'<div class="mensaje"><p>{datos}</p></div>'
    #si el dato es un diccionario con un una ky que se llame promedio
    if isinstance(datos, dict) and len(datos) == 1 and list(datos.keys())[0].startswith("promedio"):
        clave = list(datos.keys())[0]
        valor = datos[clave]
        return (
            f'<div class="mensaje">'
            f'<h2>📊 {clave.replace("_", " ").capitalize()}</h2>'
            f'<p><strong>{valor:,}</strong></p>'
            f'</div>'
        )
    #para datos que se llamen error
    if isinstance(datos, dict) and "error" in datos:
        return f'<div class="mensaje error"><p>⚠️ {datos["error"]}</p></div>'
    #si viene como diccionario, lo convierte a lista
    if isinstance(datos, dict):
        datos = [datos]
    #el principal por asi decirlo, el que imprime todos los paises segun las condiciones del usuario
    if all("cantidad" in item and "continente" in item for item in datos):
        html = '<table class="tabla-salidas">'
        html += "<thead><tr><th>Continente</th><th>Cantidad de países</th></tr></thead>"
        html += "<tbody>"
        for item in datos:
            nombre_cont = item["continente"]
            cantidad = item["cantidad"]
            html += f"<tr><td>{nombre_cont}</td><td>{cantidad}</td></tr>"
        html += "</tbody></table>"
        return html

    html = '<table class="tabla-salidas">'
    html += "<thead><tr><th>Nombre</th><th>Población</th><th>Superficie</th><th>Continente</th></tr></thead>"
    html += "<tbody>"
    #Recorre cada país y agrega una fila a la tabla con sus datos.
    for pais in datos:
        nombre = pais.get("nombre", "-")
        poblacion = pais.get("poblacion", "-")
        superficie = pais.get("superficie", "-")
        continente = pais.get("continente", "-")
        # Si la población es cero, aclara que se trata de habitantes no permanentes.
        if str(poblacion) == "0":
            poblacion = "0 (no permanentes)"
        html += f"<tr><td>{nombre}</td><td>{poblacion}</td><td>{superficie} km²</td><td>{continente}</td></tr>"

    html += "</tbody></table>"
    return html
