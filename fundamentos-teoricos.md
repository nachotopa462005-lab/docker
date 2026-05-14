# Fundamentos teóricos: imágenes por capas y Dockerfile

## Sistema de capas en Docker

Docker utiliza un sistema de capas (layers). Cada instrucción dentro de un Dockerfile crea una nueva capa.

Ejemplo:

```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
```

Docker guarda estas capas en cache para reutilizarlas y acelerar los builds.

El orden de las instrucciones es importante porque si una capa cambia, Docker vuelve a construir las siguientes.

Por ejemplo:

```dockerfile
COPY package.json .
RUN npm install
COPY . .
```

Es mejor que copiar todo primero, porque así `npm install` solo se ejecuta si cambian las dependencias.

---

# Instrucciones importantes del Dockerfile

## FROM

Define la imagen base.

```dockerfile
FROM node:20-alpine
```

---

## WORKDIR

Define el directorio de trabajo.

```dockerfile
WORKDIR /app
```

---

## COPY

Copia archivos al contenedor.

```dockerfile
COPY . .
```

---

## ADD

Parecido a `COPY`, pero también puede descomprimir archivos o descargar desde URLs.

```dockerfile
ADD archivo.tar.gz /app
```

---

## RUN

Ejecuta comandos durante el build.

```dockerfile
RUN npm install
```

---

## ENV

Define variables de entorno.

```dockerfile
ENV PORT=3000
```

---

## EXPOSE

Indica el puerto que usa la aplicación.

```dockerfile
EXPOSE 3000
```

---

## CMD

Define el comando por defecto del contenedor.

```dockerfile
CMD ["npm", "start"]
```

---

## ENTRYPOINT

Define el ejecutable principal.

```dockerfile
ENTRYPOINT ["node", "server.js"]
```

---

## ARG

Variables disponibles solo durante el build.

```dockerfile
ARG VERSION=1.0
```

---

# Diferencia entre CMD y ENTRYPOINT

- `CMD` define comandos por defecto y puede reemplazarse fácilmente.
- `ENTRYPOINT` define el proceso principal del contenedor.

También pueden usarse juntos:

```dockerfile
ENTRYPOINT ["python"]
CMD ["app.py"]
```

---

# Imagen base Alpine

Alpine Linux es una distribución muy liviana y pequeña usada mucho en Docker.

Ejemplo:

```dockerfile
FROM node:20-alpine
```

Se prefiere frente a Ubuntu o Debian porque:

- ocupa menos espacio
- descarga más rápido
- consume menos recursos
- tiene menos vulnerabilidades

La desventaja es que algunas librerías pueden no ser compatibles.

---

# Conclusión

Docker usa capas para optimizar los builds y el almacenamiento.  
El Dockerfile permite configurar cómo se construye y ejecuta un contenedor mediante instrucciones como `FROM`, `COPY`, `RUN` y `CMD`.

Además, Alpine es muy utilizada porque es más ligera y eficiente que otras imágenes base.