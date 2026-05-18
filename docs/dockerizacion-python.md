# Dockerizacion de Python con FastAPI

## API REST con FastAPI

En este proyecto se creo una API pequena con FastAPI. La API expone endpoints para comprobar el estado del servicio, consultar inventario, usar cache con Redis y guardar IPs sospechosas.

Endpoints principales:

| Metodo | Ruta | Descripcion |
|--------|------|-------------|
| GET | `/status` | Comprueba que la API funciona |
| GET | `/inventario` | Devuelve productos de ejemplo |
| GET | `/cache` | Consulta datos cacheados en Redis |
| POST | `/ips/{ip}` | Agrega una IP sospechosa a Redis |
| GET | `/ips` | Lista las IPs guardadas |

## Dockerfile

El backend se construye con una imagen `python:3.11-alpine`.

```dockerfile
FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
```

La idea es:

1. Usar una base ligera de Python.
2. Copiar dependencias.
3. Instalar FastAPI, Uvicorn y Redis.
4. Copiar el codigo.
5. Ejecutar la API en el puerto `5000`.

## Variables de entorno

La API lee la configuracion de Redis desde variables de entorno:

```python
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
```

Esto permite cambiar la configuracion sin modificar el codigo.

## Ejecucion con Docker Compose

Para levantar el proyecto:

```bash
cd python-api
cp .env.example .env
docker compose up -d --build
```

Luego se puede probar:

```bash
curl -k https://localhost:4443/status
```
