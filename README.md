![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) ![NGINX](https://img.shields.io/badge/NGINX-009639?style=for-the-badge&logo=nginx&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white) ![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)

# Infraestructura Docker con FastAPI, Redis y NGINX

> Proyecto practico de dockerizacion de una API Python usando Docker Compose, Redis como cache y NGINX como proxy inverso con HTTPS.

| Despliegue | URL |
|------------|-----|
| Local con Docker Compose | https://localhost:4443 |

---

## Caracteristicas

- API REST hecha con FastAPI.
- Redis usado para cache y almacenamiento simple de IPs.
- NGINX como proxy inverso con redireccion HTTP a HTTPS.
- Healthchecks para controlar el arranque correcto de los servicios.
- Red interna de Docker para aislar backend, Redis y proxy.

---

## Tecnologias

| Backend | Uso |
|---------|-----|
| Python 3.11 | Lenguaje principal de la API |
| FastAPI | Creacion de endpoints REST |
| Uvicorn | Servidor ASGI para ejecutar FastAPI |

| Infraestructura | Uso |
|-----------------|-----|
| Docker | Construccion de contenedores |
| Docker Compose | Orquestacion de servicios |
| NGINX | Proxy inverso, HTTPS y rate limiting |
| Redis | Cache y almacenamiento en memoria |

| Auxiliares | Uso |
|------------|-----|
| Healthchecks | Verificacion del estado de backend y Redis |
| Variables de entorno | Configuracion sin exponer secretos |
| Certificados locales | Prueba de HTTPS en entorno local |

---

## Estructura del proyecto

```text
docker/
|-- docs/
|   |-- docker-teoria.md
|   |-- fundamentos-teoricos.md
|   |-- teoria-NGINX.md
|   |-- dockerizacion-python.md
|   |-- health-checks.md
|   |-- docker-stats.md
|   |-- explicacion-volumenes.md
|   `-- explicacion-env.md
|-- python-api/
|   |-- certs/
|   |   `-- .gitkeep
|   |-- static/
|   |   `-- index.html
|   |-- .dockerignore
|   |-- .env.example
|   |-- Dockerfile
|   |-- docker-compose.yml
|   |-- main.py
|   |-- nginx.conf
|   `-- requirements.txt
|-- .gitignore
`-- README.md
```

---

## Descargar y ejecutar

```bash
git clone https://github.com/nachotopa462005-lab/docker.git
cd docker/python-api
cp .env.example .env
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout certs/key.pem -out certs/cert.pem -subj "/CN=localhost"
docker compose up -d --build
```

En Windows PowerShell, si `cp` no esta disponible:

```powershell
Copy-Item .env.example .env
```

Los certificados locales no se suben al repositorio. Se generan para probar HTTPS en desarrollo.

---

## Probar la aplicacion

```bash
curl -k https://localhost:4443/status
curl -k https://localhost:4443/inventario
curl -k https://localhost:4443/cache
```

Tambien se puede abrir en el navegador:

- https://localhost:4443/status
- https://localhost:4443/inventario
- https://localhost:4443/static/

El certificado es local, por eso el navegador puede mostrar una advertencia de seguridad.

---

## Infraestructura

El archivo `docker-compose.yml` levanta tres servicios:

- `backend`: API FastAPI ejecutada con Uvicorn en el puerto interno `5000`.
- `redis`: base en memoria protegida con password desde variables de entorno.
- `proxy`: NGINX expuesto en `8088` para HTTP y `4443` para HTTPS.

NGINX recibe las peticiones externas, redirige HTTP a HTTPS y envia el trafico hacia el backend usando la red interna `app-network`.

---

## Comandos utiles

```bash
docker compose ps
docker compose logs -f
docker compose down
docker compose build backend
docker compose up -d --scale backend=3
docker stats
```

---

## Documentacion

La teoria del trabajo esta separada en la carpeta `docs/`, donde se explican Docker, Dockerfile, volumenes, variables de entorno, NGINX, healthchecks y comandos de administracion.
