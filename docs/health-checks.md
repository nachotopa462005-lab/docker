# Importancia de los healthchecks en produccion

Los healthchecks permiten saber si un contenedor esta realmente funcionando y listo para recibir peticiones.

Un contenedor puede estar iniciado, pero la aplicacion interna puede seguir cargando o fallar por dentro. Por eso no alcanza con ver que el contenedor este en estado `running`.

En este proyecto hay healthchecks para:

- `backend`: comprueba el endpoint `/status`.
- `redis`: ejecuta `redis-cli ping`.

Ejemplo del backend:

```yaml
healthcheck:
  test: ["CMD", "python", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:5000/status')"]
  interval: 10s
  timeout: 5s
  retries: 5
```

Docker Compose tambien usa estos checks en `depends_on`:

```yaml
depends_on:
  redis:
    condition: service_healthy
```

Esto hace que el backend espere a Redis y que NGINX espere al backend. Es util porque evita errores de conexion al iniciar toda la infraestructura.

En produccion, los healthchecks ayudan a detectar fallos, reiniciar servicios y mejorar la estabilidad del sistema.
