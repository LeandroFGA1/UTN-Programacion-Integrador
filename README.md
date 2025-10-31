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
- **limpar** Restaurar tabla original (limpiar filtros y ordenamientos)
---

## 📊 Ejemplos de entrada, salida y flujo de filtros

A continuación se presentan ejemplos del comportamiento de la aplicación y cómo se aplican los filtros y ordenamientos de manera secuencial:

1. **Búsqueda de países por nombre**  
   - Entrada parcial: `"arge"` → Resultado: **Argelia** y **Argentina**  
   - Entrada exacta: `"Argentina"` → Resultado: **Argentina**  
   Esto permite realizar búsquedas flexibles, que coincidan con parte del nombre o con el nombre completo del país.

2. **Flujo de filtros secuenciales**  
   - Se aplica el filtro por **continente**: `"África"` → Se muestran 59 países  
   - Luego se filtra por **población** en el rango `4.000` a `400.000` → Resultado: 4 países  
   - Posteriormente se filtra por **superficie** entre `0` y `500 km²` → Resultado: 3 países  
   - Finalmente, se aplica el **ordenamiento por mayor/menor población** → Resultado: 2 países  

3. **Limitaciones del flujo de filtros**  
   - Después de varias operaciones secuenciales, para aplicar nuevos filtros o realizar búsquedas diferentes, es necesario **utilizar el botón “Limpiar”**.  
   - Esto restaura el CSV original y permite iniciar un nuevo flujo de filtrado u ordenamiento.

> 🔹 Esta secuencia demuestra cómo la aplicación mantiene la coherencia de los datos y asegura que cada acción tenga un efecto predecible sobre la tabla de países.




---
## 📝 Comentarios y consideraciones del proyecto

- **Manejo del CSV y filtros:**  
  Inicialmente, la aplicación generaba una **copia del CSV** y manipulaba esa lista cada vez que se activaba un botón.  
  Esto provocaba que, por ejemplo, al filtrar por continente y luego por población, los resultados del segundo filtro se aplicaran sobre **todos los países originales**, sin considerar el filtro anterior.  
  Para mantener una **secuencia lógica de acciones**, se decidió **reconstruir el CSV después de cada operación**.  
  De esta forma, cada acción tiene sentido independiente y el botón de "Limpiar" puede restaurar el CSV original correctamente, ya sea recargando desde el archivo o usando una copia de seguridad interna.

- **Tratamiento de la Antártida:**  
  Aunque existen territorios reclamados en la Antártida, **no se consideran países soberanos**, y por tratados internacionales el continente es administrado de manera compartida por varios países (entre ellos Argentina y Chile).  
  Por esta razón, la Antártida **no fue incluida en el CSV** como país o continente activo.

- **Campo "independencia":**  
  En el CSV se incluyó un campo llamado `"independencia"`, con la intención de **diferenciar países independientes de territorios no independientes**.  
  Sin embargo, **no se implementó su funcionalidad** en la aplicación debido a limitaciones de tiempo.
---






---

## Tecnologías utilizadas

| Tecnología   | Descripción             |
| Python 3.11 | Lógica y manejo de datos |
| Flask       | Backend web            |
| Docker      | Contenedor del entorno |
| CSV         | Fuente de datos        |
| HTML / CSS  | Interfaz del usuario   |


---


## 👥 Participación de los integrantes

| Integrante         | Responsabilidades principales |
|-------------------|-------------------------------|
| Rodrigo Gatica     | Desarrollo del **HTML y CSS**, diseño del **aspecto visual** de la aplicación y la interfaz de usuario. |
| Leandro Aucache    | Configuración de **Docker**, implementación de **backend**, **filtros**, **ordenamientos**, **buscador**, **estadísticas**, pruebas y elaboración del **informe final**. Edicion de video, funcionalidad del **aspecto visual** |


Proyecto académico para **UTN - Universidad Tecnológica Nacional**  

✅ *Listo para ejecutarse en cualquier entorno con Docker y Python 3.11.*
