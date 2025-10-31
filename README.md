# UTN - Programación Integrador

Este proyecto fue desarrollado como **Trabajo Práctico Integrador (TPI)**.  
Gestiona información de países a partir de un archivo **CSV**, mostrando y analizando datos como:

- Nombre del país  
- Población  
- Superficie (km²)  
- Continente

---

## Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener instalados:

### Docker
[Descargar Docker](https://www.docker.com/products/docker-desktop/)

> ⚙️ *Recuerda activar la virtualización de hardware desde la BIOS:*  
> - En **Intel**: habilita `Intel Virtualization Technology (VT-x)`  
> - En **AMD**: habilita `SVM Mode` o `AMD-V`

### Python 3.11
[Descargar Python 3.11](https://www.python.org/downloads/release/python-3110/)

### IDE recomendado
- Visual Studio Code

---

## Ejecución del proyecto

### 1️⃣ Clonar o descargar el repositorio

```bash
git clone https://github.com/LeandroFGA1/UTN-Programacion-Integrador.git
```

O descargar el ZIP directamente desde GitHub y descomprimirlo.

---

### 2️⃣ Construir la imagen Docker

Dentro del directorio del proyecto, ejecuta:

```bash
docker build -t tpi-flask-app .
```

---

### 3️⃣ Ejecutar el contenedor

```bash
docker run -p 5000:5000 tpi-flask-app
```

Cuando se inicie correctamente, verás algo como:

```bash
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
```

---

### 4️⃣ Abrir en el navegador

Accede a la aplicación desde:

```bash
http://127.0.0.1:5000
```

---

## Funcionalidades principales

- Visualización completa del archivo CSV  
- Búsqueda de países por nombre  
- Filtrado por continente  
- Filtrado por población o superficie dentro de un rango  
- Ordenamientos personalizados:
  - Nombre del país (A–Z / Z–A)  
  - Población (mayor o menor)  
  - Superficie (mayor o menor)  
- Estadísticas disponibles:
  - Países con menor y mayor población  
  - Promedio de población mundial  
  - Promedio de superficie mundial  
  - Cantidad de países por continente  
- Restaurar tabla original (limpiar filtros y ordenamientos)

---

## Tecnologías utilizadas

| Tecnología   | Descripción             |
| Python 3.11 | Lógica y manejo de datos |
| Flask       | Backend web            |
| Docker      | Contenedor del entorno |
| CSV         | Fuente de datos        |
| HTML / CSS  | Interfaz del usuario   |


---

Proyecto académico para **UTN - Universidad Tecnológica Nacional**  

✅ *Listo para ejecutarse en cualquier entorno con Docker y Python 3.11.*
