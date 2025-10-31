from flask import Flask, render_template,request
from creacion_csv import crear_csv,BASE_DIRECTORIO,CSV,PARAMETROS
from auxiliares import duplicado_csv
from generador_html import generar_html_salidas
from consignas import buscar_pais,filtrar_continentes,filtrar_rango,ordenar_paises,min_max_poblacion,promedio_poblacion,promedio_superficie,paises_por_continente
import csv
import os
app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)

crear_csv()

@app.route('/')
def home():
    paises = duplicado_csv()
    html_salida = generar_html_salidas(paises)
    return render_template('index.html',html_salida=html_salida)

@app.route('/buscar')
def buscar():
    nombre = request.args.get('pais', '')
    resultado = buscar_pais(nombre)
    html_salida = generar_html_salidas(resultado)
    return render_template('index.html', html_salida=html_salida)

@app.route('/filtrar_continente')
def filtrar_continente():
    continente = request.args.get('continente', '')
    resultado = filtrar_continentes(continente)
    html_salida = generar_html_salidas(resultado)
    return render_template('index.html', html_salida=html_salida)


@app.route('/filtrar_poblacion')
def filtrar_poblacion_ruta():
    minimo = int(request.args.get('min', 0))
    maximo = int(request.args.get('max', 0))
    resultado = filtrar_rango(minimo, maximo, "poblacion")
    html_salida = generar_html_salidas(resultado)
    return render_template('index.html', html_salida=html_salida)


@app.route('/filtrar_superficie')
def filtrar_superficie_ruta():
    minimo = int(request.args.get('min', 0))
    maximo = int(request.args.get('max', 0))
    resultado = filtrar_rango(minimo, maximo, "superficie")
    html_salida = generar_html_salidas(resultado)
    return render_template('index.html', html_salida=html_salida)

@app.route('/ordenar')
def ordenar():
    criterio = request.args.get('criterio', '')
    resultado = ordenar_paises(criterio) 
    html_salida = generar_html_salidas(resultado)
    return render_template('index.html', html_salida=html_salida)

@app.route("/borrar")
def borrar():
    if os.path.exists(CSV):
        os.remove(CSV)
    crear_csv()
    paises = duplicado_csv()
    html_salida = generar_html_salidas(paises)
    return render_template('index.html',html_salida=html_salida)

@app.route("/estadisticas")
def estadisticas():
    tipo = request.args.get("tipo")

    if not tipo:
        html_salida = generar_html_salidas({"error": "Tipo no especificado"})
        return render_template("index.html", html_salida=html_salida)

    if tipo == "maxmin_poblacion":
        resultado = min_max_poblacion()
        html_salida = generar_html_salidas(resultado)
        return render_template("index.html", html_salida=html_salida)

    elif tipo == "prom_poblacion":
        resultado = promedio_poblacion()
        html_salida = generar_html_salidas(resultado)
        return render_template("index.html", html_salida=html_salida)

    elif tipo == "prom_superficie":
        resultado = promedio_superficie()
        html_salida = generar_html_salidas(resultado)
        return render_template("index.html", html_salida=html_salida)


    elif tipo == "paises_continente":
        resultado = paises_por_continente()
        html_salida = generar_html_salidas(resultado)
        return render_template("index.html", html_salida=html_salida)

    html_salida = generar_html_salidas({"error": f"Tipo desconocido: {tipo}"})
    return render_template("index.html", html_salida=html_salida)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
