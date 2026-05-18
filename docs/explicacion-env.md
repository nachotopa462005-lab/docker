# Seguridad de secretos en Docker

No conviene escribir secretos directamente en un `Dockerfile` o en `docker-compose.yml`.

Ejemplos de secretos:

- Passwords.
- Tokens.
- Claves API.
- Credenciales de bases de datos.
- Claves privadas.

Ejemplo inseguro:

```yaml
environment:
  REDIS_PASSWORD: 1234
```

El problema es que esa informacion puede subirse a GitHub o quedar guardada en el historial de Git.

## Uso de variables de entorno

La mejor opcion para este proyecto es usar un archivo `.env` local:

```env
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_PASSWORD=tu_password
```

Docker Compose lee esas variables asi:

```yaml
environment:
  REDIS_PASSWORD: ${REDIS_PASSWORD}
```

## Archivo .env.example

El archivo `.env` real no se sube al repositorio. En su lugar se deja `.env.example` como plantilla.

Asi otra persona puede copiarlo:

```bash
cp .env.example .env
```

Y despues cambiar los valores si hace falta.

Esto mejora la seguridad porque separa configuracion sensible del codigo fuente.
