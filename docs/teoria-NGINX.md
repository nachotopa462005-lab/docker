# Fundamentos teoricos: proxy inverso y NGINX

## Que es un proxy inverso

Un proxy inverso es un servidor que recibe las peticiones de los clientes y las envia al servidor interno correspondiente.

La diferencia con un proxy directo es:

- Proxy directo: representa al cliente.
- Proxy inverso: representa al servidor.

En este proyecto, NGINX actua como proxy inverso porque recibe las peticiones externas y las envia al backend FastAPI.

---

## Por que se usa NGINX delante de una aplicacion

NGINX se usa delante de una aplicacion porque ayuda a mejorar seguridad, orden y rendimiento.

Puede encargarse de:

- HTTPS y certificados SSL.
- Redireccion de HTTP a HTTPS.
- Rate limiting para limitar muchas peticiones.
- Servir archivos estaticos.
- Ocultar el backend real.
- Enviar trafico hacia uno o varios servicios internos.

Asi la API no queda expuesta directamente al exterior.

---

## Que es un upstream en NGINX

Un `upstream` define uno o varios servidores backend a los que NGINX puede enviar peticiones.

Ejemplo del proyecto:

```nginx
upstream backend {
    server backend:5000;
}
```

Docker Compose permite que NGINX encuentre el servicio `backend` usando el nombre del servicio dentro de la red interna.

---

## Que es un server block

Un `server block` define como responde NGINX en un puerto o dominio.

En el proyecto hay dos bloques principales:

- Uno escucha en `80` y redirige a HTTPS.
- Otro escucha en `443 ssl` y envia las peticiones al backend.

Ejemplo:

```nginx
server {
    listen 443 ssl;

    location / {
        proxy_pass http://backend;
    }
}
```

---

## Por que NGINX es mas eficiente que Apache

NGINX usa un modelo asincrono y basado en eventos. Esto le permite manejar muchas conexiones al mismo tiempo usando pocos recursos.

Apache tradicionalmente usa procesos o hilos por conexion, lo que puede consumir mas memoria cuando hay mucho trafico.

Por eso NGINX suele utilizarse mucho en APIs, microservicios, balanceo de carga y servidores con muchas peticiones simultaneas.
