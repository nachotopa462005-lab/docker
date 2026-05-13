# Teoría de Docker

## Diferencia entre una máquina virtual y un contenedor Docker

### Máquina virtual (VM)

Una máquina virtual emula un computador completo mediante un hipervisor. Cada VM incluye:

- Un sistema operativo completo.
- Sus propias librerías y dependencias.
- Aplicaciones instaladas sobre ese sistema operativo.

Las máquinas virtuales consumen más recursos porque cada una necesita memoria, CPU y almacenamiento para su sistema operativo independiente.

### Contenedor Docker

Un contenedor Docker es una forma ligera de virtualización a nivel de sistema operativo. En lugar de incluir un sistema operativo completo, los contenedores:

- Comparten el kernel del sistema operativo del host.
- Aíslan procesos, red y sistema de archivos.
- Incluyen únicamente las dependencias necesarias para la aplicación.

Esto hace que los contenedores sean mucho más rápidos y ligeros que las máquinas virtuales.

## ¿Qué recursos comparte el contenedor con el host?

Los contenedores Docker comparten principalmente:

- El kernel del sistema operativo del host.
- Recursos físicos como CPU, memoria y disco.
- Interfaces de red del host (virtualizadas mediante namespaces).

## ¿Qué aísla un contenedor?

Docker utiliza mecanismos del kernel Linux para aislar:

- Procesos.
- Sistema de archivos.
- Red.
- Usuarios.
- Recursos de CPU y memoria.

Este aislamiento se logra mediante tecnologías como:

- Namespaces.
- Cgroups.
- Union File Systems.

---

# Conceptos clave de Docker

## Imagen

Una imagen Docker es una plantilla inmutable que contiene:

- El sistema base.
- Librerías.
- Dependencias.
- Código de la aplicación.
- Configuración necesaria para ejecutarla.

Las imágenes se utilizan para crear contenedores.

Ejemplo:
```bash
docker pull nginx
```

## Contenedor

Un contenedor es una instancia en ejecución de una imagen Docker.

Puede:

- Ejecutarse.
- Detenerse.
- Reiniciarse.
- Eliminarse.

Cada contenedor tiene un entorno aislado.

## Dockerfile

Un Dockerfile es un archivo de texto con instrucciones para construir una imagen Docker automáticamente.

Ejemplo:
```Dockerfile
FROM node:20
WORKDIR /app
COPY . .
RUN npm install
CMD ["npm", "start"]
```

## Docker Hub

Docker Hub es un registro público de imágenes Docker.

Permite:

- Descargar imágenes.
- Compartir imágenes.
- Publicar imágenes propias.

Sitio oficial:
https://hub.docker.com/

## Capa (Layer)

Las imágenes Docker están formadas por capas.

Cada instrucción del Dockerfile genera una nueva capa.

Ventajas:

- Reutilización.
- Caché eficiente.
- Menor consumo de almacenamiento.

## Registro (Registry)

Un registry es un servicio donde se almacenan imágenes Docker.

Puede ser:

- Público.
- Privado.

Ejemplos:

- Docker Hub.
- GitHub Container Registry.
- Amazon ECR.

---

# Ciclo de vida de un contenedor

## 1. Creado (Created)

El contenedor existe pero aún no está ejecutándose.

Ejemplo:
```bash
docker create nginx
```

## 2. En ejecución (Running)

El contenedor está activo y ejecutando procesos.

Ejemplo:
```bash
docker start <contenedor>
```

## 3. Pausado (Paused)

Los procesos del contenedor quedan temporalmente suspendidos.

Ejemplo:
```bash
docker pause <contenedor>
```

## 4. Detenido (Stopped)

El contenedor deja de ejecutarse, pero sigue existiendo.

Ejemplo:
```bash
docker stop <contenedor>
```

## 5. Eliminado (Removed)

El contenedor es borrado completamente.

Ejemplo:
```bash
docker rm <contenedor>
```

## ¿Qué ocurre con los datos cuando un contenedor se elimina?

Cuando un contenedor se elimina:

- Los datos almacenados dentro del contenedor se pierden.
- Los volúmenes Docker externos permanecen intactos.
- Las imágenes utilizadas para crearlo no se eliminan automáticamente.

Por eso, para datos persistentes se utilizan volúmenes.

---

# Relación entre Kernel, Docker Engine y Contenedores

## Descripción del diagrama

```text
+--------------------------------------------------+
|                 Sistema Operativo Host           |
|--------------------------------------------------|
|                     Kernel Linux                 |
+--------------------------------------------------+
|                  Docker Engine                   |
|--------------------------------------------------|
|  Contenedor A   |  Contenedor B  | Contenedor C |
|-----------------|----------------|--------------|
| App + Librerías | App + Librerías| App + Libr. |
+--------------------------------------------------+
```

## Explicación

1. El sistema operativo host contiene el kernel Linux.
2. Docker Engine se ejecuta sobre el sistema operativo host.
3. Los contenedores utilizan Docker Engine para funcionar.
4. Todos los contenedores comparten el mismo kernel del host.
5. Cada contenedor mantiene aisladas sus aplicaciones, procesos y dependencias.
