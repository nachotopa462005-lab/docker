# Gestion avanzada y limpieza del entorno

Durante la practica se uso Docker Compose para administrar toda la infraestructura.

## Levantar servicios

```bash
docker compose up -d
```

Este comando inicia los servicios en segundo plano:

- backend
- redis
- proxy NGINX

## Detener servicios

```bash
docker compose down
```

Elimina los contenedores y la red creada por Compose. Si hubiera volumenes nombrados, se conservarian salvo que se use `-v`.

## Reconstruir un servicio

```bash
docker compose build backend
```

Sirve para reconstruir solo el backend cuando cambia el Dockerfile, las dependencias o el codigo.

## Escalar backend

```bash
docker compose up -d --scale backend=3
```

Este comando crea varias instancias del backend. En un caso real esto puede ayudar a distribuir carga, aunque la configuracion de puertos y proxy debe estar preparada para ese escenario.

## Ver consumo de recursos

```bash
docker stats
```

Permite ver CPU, memoria, red y disco usados por cada contenedor en tiempo real.

## Limpieza del sistema

```bash
docker system prune -a
```

Elimina contenedores detenidos, imagenes sin uso y cache de builds. Hay que usarlo con cuidado porque puede borrar imagenes que despues habra que descargar o construir otra vez.
