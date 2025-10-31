# Imagen base
FROM python:3.11-slim

# Carpeta de trabajo
WORKDIR /app

# Copiar requerimientos y instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar la app
COPY app/ .
COPY static/ ./static

# Exponer el puerto
EXPOSE 5000

# Comando para correr la app
CMD ["python", "app.py"]
