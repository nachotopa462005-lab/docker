# Gestión avanzada y limpieza del entorno

Durante esta práctica se utilizó Docker Compose para gestionar toda la infraestructura del proyecto.

Para levantar todos los servicios se utilizó:

```bash
docker compose up -d
```

Con este comando se iniciaron el backend, Redis y NGINX en segundo plano.

Para detener la infraestructura:

```bash
docker compose down
```

También se practicó la reconstrucción de un único servicio sin afectar a los demás:

```bash
docker compose build backend
```

Esto permite actualizar solo el backend sin reiniciar Redis o NGINX.

Luego se escaló el servicio backend a múltiples instancias:

```bash
docker compose up -d --scale backend=3
```

Con esto Docker creó varias instancias del backend para mejorar disponibilidad y distribución de carga.

Para observar el uso de recursos en tiempo real se utilizó:

```bash
docker stats# Gestión avanzada y limpieza del entorno

Docker Compose permite administrar fácilmente el ciclo de vida completo de una infraestructura.

Algunos comandos importantes son:

- `docker compose up -d`: levanta los servicios
- `docker compose stop`: detiene contenedores
- `docker compose start`: inicia contenedores existentes
- `docker compose restart`: reinicia servicios
- `docker compose down`: elimina contenedores y redes

También es posible reconstruir solo un servicio específico usando:

```bash
docker compose build backend
```

Este comando permitió visualizar consumo de CPU, memoria y red de cada contenedor.

Finalmente se realizó limpieza del sistema eliminando recursos no utilizados:

```bash
docker system prune -a
```

Este comando eliminó imágenes, cachés y contenedores innecesarios.

Teniendo únicamente los contenedores e imágenes utilizados en esta práctica,  se liberaron entre 1 GB y 2 GB de espacio, principalmente debido a imágenes de Python, NGINX, Redis y caché de builds anteriores.