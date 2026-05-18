# Teoria de Docker

## Diferencia entre una maquina virtual y un contenedor Docker

Una maquina virtual emula un equipo completo. Incluye su propio sistema operativo, librerias y recursos asignados. Por eso suele consumir mas memoria, CPU y almacenamiento.

Un contenedor Docker es mas liviano porque comparte el kernel del sistema operativo del host. Dentro del contenedor solo se empaqueta la aplicacion y sus dependencias.

En resumen:

| Maquina virtual | Contenedor Docker |
|-----------------|-------------------|
| Tiene sistema operativo completo | Comparte el kernel del host |
| Es mas pesada | Es mas liviano |
| Tarda mas en iniciar | Inicia rapido |
| Usa mas recursos | Usa menos recursos |

## Que recursos comparte el contenedor con el host

Un contenedor comparte con el host:

- Kernel del sistema operativo.
- CPU.
- Memoria RAM.
- Disco.
- Red, aunque Docker la organiza con redes virtuales.

Aunque comparta recursos, Docker mantiene cada contenedor aislado para que una aplicacion no interfiera directamente con otra.

## Que aisla un contenedor

Docker aisla:

- Procesos.
- Sistema de archivos.
- Red.
- Variables de entorno.
- Usuarios y permisos.
- Uso de CPU y memoria.

Para lograrlo usa tecnologias del kernel como namespaces y cgroups.

---

## Conceptos clave de Docker

### Imagen

Una imagen es una plantilla de solo lectura que contiene todo lo necesario para crear un contenedor.

Ejemplo:

```bash
docker pull nginx
```

### Contenedor

Un contenedor es una instancia en ejecucion de una imagen. Se puede iniciar, detener, reiniciar y eliminar.

Ejemplo:

```bash
docker run nginx
```

### Dockerfile

Un Dockerfile es un archivo con instrucciones para construir una imagen.

Ejemplo:

```dockerfile
FROM python:3.11-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Docker Hub

Docker Hub es un repositorio publico de imagenes. Desde ahi se pueden descargar imagenes como `nginx`, `redis`, `python` o `mysql`.

### Capa o layer

Las imagenes Docker se construyen por capas. Cada instruccion del Dockerfile genera una capa nueva. Esto permite reutilizar cache y hacer builds mas rapidos.

### Registry

Un registry es un lugar donde se guardan imagenes Docker. Puede ser publico o privado.

Ejemplos:

- Docker Hub.
- GitHub Container Registry.
- Amazon ECR.

---

## Ciclo de vida de un contenedor

1. `created`: el contenedor fue creado pero todavia no inicio.
2. `running`: el contenedor esta ejecutandose.
3. `paused`: el contenedor esta pausado temporalmente.
4. `stopped`: el contenedor esta detenido.
5. `removed`: el contenedor fue eliminado.

Ejemplos:

```bash
docker create nginx
docker start <contenedor>
docker stop <contenedor>
docker rm <contenedor>
```

## Que pasa con los datos al eliminar un contenedor

Si los datos estan dentro del contenedor, se pierden al eliminarlo. Para evitarlo se usan volumenes o bind mounts.

Los volumenes son la mejor opcion para datos importantes, porque Docker los guarda fuera del ciclo de vida del contenedor.

---

## Relacion entre Kernel, Docker Engine y contenedores

```text
Sistema operativo host
└── Kernel
    └── Docker Engine
        ├── Contenedor backend
        ├── Contenedor redis
        └── Contenedor nginx
```

El sistema operativo tiene el kernel. Docker Engine usa ese kernel para crear y administrar contenedores. Cada contenedor ejecuta su aplicacion aislada, pero todos comparten la base del host.
