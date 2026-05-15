# Fundamentos teóricos: proxy inverso y NGINX

## ¿Qué es un proxy inverso?

Un proxy inverso es un servidor que se coloca delante de una aplicación o varios servidores y recibe todas las peticiones de los clientes antes de enviarlas al servidor real.

La diferencia con un proxy directo es que:

- el proxy directo representa al cliente
- el proxy inverso representa al servidor

En un proxy directo, el cliente usa el proxy para acceder a internet.  
En cambio, en un proxy inverso, los clientes no saben realmente qué servidor responde por detrás.

---

## ¿Por qué se usa NGINX delante de una aplicación?

NGINX suele colocarse delante de aplicaciones en producción porque mejora el rendimiento y la seguridad.

Algunas ventajas importantes son:

- gestión de certificados SSL/HTTPS
- balanceo de carga
- caché de contenido
- rate limiting para limitar peticiones
- protección de la aplicación real
- manejo eficiente de muchas conexiones

También permite que la aplicación quede aislada y no expuesta directamente a internet.

---

## ¿Qué es un upstream en NGINX?

Un upstream es un grupo de servidores backend al que NGINX puede enviar tráfico.

Por ejemplo, si hay varias instancias de una API, NGINX puede repartir las peticiones entre ellas.

Ejemplo:

```nginx
upstream backend {
    server app1:5000;
    server app2:5000;
}
```

Esto se usa mucho para balanceo de carga y alta disponibilidad.

---

## ¿Qué es un server block?

Un server block es una configuración que define cómo NGINX responde a determinadas peticiones.

Dentro del server block se configura:

- el puerto
- el dominio
- rutas
- proxy_pass
- certificados SSL

Ejemplo:

```nginx
server {
    listen 80;

    location / {
        proxy_pass http://backend;
    }
}
```

---

## ¿Por qué NGINX es más eficiente que Apache?

NGINX suele ser más eficiente que Apache cuando hay mucho tráfico porque usa una arquitectura asíncrona y basada en eventos.

Apache normalmente crea procesos o hilos por conexión, lo que consume más memoria.

En cambio, NGINX puede manejar miles de conexiones simultáneas usando pocos recursos.

Por eso NGINX es muy utilizado en:

- aplicaciones grandes
- APIs
- microservicios
- sitios con mucho tráfico

Además, suele consumir menos RAM y responder más rápido bajo carga alta.