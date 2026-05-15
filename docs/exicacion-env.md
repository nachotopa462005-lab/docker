# Seguridad de secretos en Docker

Nunca se deben incluir secretos directamente en un `Dockerfile` o en un archivo `docker-compose.yml` en texto plano porque representa un riesgo importante de seguridad.

Los secretos pueden ser:

- contraseñas
- claves API
- tokens
- credenciales de bases de datos
- claves privadas

Si estos datos se escriben directamente dentro del proyecto, cualquier persona con acceso al repositorio podría verlos fácilmente.

Ejemplo inseguro:

```yaml
environment:
  REDIS_PASSWORD: 1234
```

Esto genera varios problemas:

- Los secretos pueden subirse accidentalmente a GitHub.
- Las credenciales pueden quedar almacenadas en el historial de Git incluso después de borrarlas.
- Otros desarrolladores podrían acceder a información sensible.
- Las imágenes Docker pueden contener esos secretos internamente.
- Si la imagen se publica en Docker Hub, las credenciales podrían quedar expuestas públicamente.

Por este motivo, la mejor práctica es utilizar variables de entorno mediante archivos `.env`.

Ejemplo:

```env
REDIS_PASSWORD=mi_password
```

Luego, Docker Compose puede leer esas variables:

```yaml
environment:
  REDIS_PASSWORD: ${REDIS_PASSWORD}
```

Además, el archivo `.env` debe agregarse al `.gitignore` para evitar que se suba al repositorio:

```gitignore
.env
```

También es recomendable crear un archivo `.env.example` que funcione como plantilla para otros desarrolladores, pero sin incluir secretos reales.

Ejemplo:

```env
REDIS_PASSWORD=tu_password
```

De esta manera:

- los secretos quedan separados del código
- se mejora la seguridad del proyecto
- se evita exponer información sensible
- se facilita la configuración en distintos entornos
- se siguen buenas prácticas de desarrollo y despliegue