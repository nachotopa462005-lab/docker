# Volumen nombrado vs bind mount en Docker

## Volumen nombrado

Un volumen nombrado es administrado por Docker. Se usa para guardar datos persistentes sin depender directamente de una carpeta del proyecto.

Conviene usarlo cuando:

- Se quiere persistencia de datos.
- No hace falta editar los archivos desde el host.
- Se busca una opcion mas portable.
- Se quiere evitar perder datos al recrear contenedores.

Ejemplo:

```bash
docker volume create inventario-data
docker run -v inventario-data:/app/data python-api
```

## Bind mount

Un bind mount conecta una carpeta del host con una carpeta dentro del contenedor.

Conviene usarlo cuando:

- Se esta desarrollando localmente.
- Se quiere ver cambios del codigo sin reconstruir todo.
- Se necesita compartir archivos concretos con el contenedor.

Ejemplo:

```bash
docker run -v ./static:/usr/share/nginx/html nginx
```

## Diferencia principal

| Volumen nombrado | Bind mount |
|------------------|------------|
| Lo administra Docker | Usa una carpeta del host |
| Mejor para produccion | Mejor para desarrollo |
| Mas portable | Depende mas del sistema local |
| Menos acoplado al proyecto | Mas facil de editar manualmente |

En este proyecto se usan bind mounts para montar `nginx.conf`, `certs` y `static` dentro del contenedor NGINX.
