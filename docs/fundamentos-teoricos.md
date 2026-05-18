# Fundamentos teoricos: imagenes por capas y Dockerfile

## Sistema de capas en Docker

Docker construye las imagenes por capas. Cada instruccion del Dockerfile crea una capa nueva.

Ejemplo:

```dockerfile
FROM python:3.11-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
```

Docker guarda estas capas en cache. Si una capa no cambia, Docker puede reutilizarla y el build tarda menos.

Por eso conviene copiar primero `requirements.txt`, instalar dependencias y despues copiar el resto del codigo. Asi, si solo cambia el codigo, no hace falta reinstalar todas las dependencias.

---

## Instrucciones importantes del Dockerfile

### FROM

Define la imagen base.

```dockerfile
FROM python:3.11-alpine
```

### WORKDIR

Define la carpeta de trabajo dentro del contenedor.

```dockerfile
WORKDIR /app
```

### COPY

Copia archivos desde el proyecto hacia la imagen.

```dockerfile
COPY . .
```

### ADD

Tambien copia archivos, pero ademas puede descomprimir archivos o descargar contenido desde una URL. Normalmente se recomienda usar `COPY` si no se necesita esa funcion extra.

### RUN

Ejecuta comandos durante la construccion de la imagen.

```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```

### ENV

Define variables de entorno dentro de la imagen.

```dockerfile
ENV PORT=5000
```

### EXPOSE

Documenta el puerto que usa la aplicacion.

```dockerfile
EXPOSE 5000
```

### CMD

Define el comando por defecto que se ejecuta al iniciar el contenedor.

```dockerfile
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
```

### ENTRYPOINT

Define el ejecutable principal del contenedor. Se usa cuando se quiere que el contenedor siempre arranque con un comando fijo.

### ARG

Define variables disponibles solo durante el build.

```dockerfile
ARG VERSION=1.0
```

---

## Diferencia entre CMD y ENTRYPOINT

`CMD` indica el comando por defecto y se puede reemplazar facilmente al ejecutar el contenedor.

`ENTRYPOINT` fija el ejecutable principal. Se suele usar cuando el contenedor funciona como una herramienta o comando.

---

## Imagen base Alpine

Alpine Linux es una distribucion muy liviana. En este proyecto se usa `python:3.11-alpine` para que la imagen sea mas pequena y rapida de descargar.

Ventajas:

- Ocupa menos espacio.
- Tiene menos paquetes instalados.
- Reduce superficie de ataque.
- Hace que el contenedor sea mas ligero.

Desventaja: algunas librerias pueden requerir paquetes extra para compilar o funcionar.
