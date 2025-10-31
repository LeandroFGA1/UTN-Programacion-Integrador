# Imagen base
FROM python:3.11-slim

# Carpeta de trabajo
WORKDIR /app

# Copiar requerimientos y instalarlos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el contenido
COPY app/ .
COPY static/ ./static

# Puerto de salida
EXPOSE 5000

# Comando para inicial la app
CMD ["python", "app.py"]
