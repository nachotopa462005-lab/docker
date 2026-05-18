from fastapi import FastAPI
import redis
import os
import json

app = FastAPI()

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

r = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
    decode_responses=True
)

inventario = [
    {"id": 1, "producto": "Teclado", "stock": 10},
    {"id": 2, "producto": "Mouse", "stock": 5}
]


@app.get("/status")
def status():
    return {"estado": "API funcionando"}


@app.get("/inventario")
def get_inventario():
    return inventario


@app.get("/cache")
def cache_logs():

    cache = r.get("logs_cache")

    if cache:
        return {
            "fuente": "redis",
            "data": json.loads(cache)
        }

    logs = {
        "errores": 15,
        "warnings": 8,
        "ips": ["192.168.1.10", "10.0.0.5"]
    }

    r.set("logs_cache", json.dumps(logs))

    return {
        "fuente": "api",
        "data": logs
    }


@app.post("/ips/{ip}")
def add_ip(ip: str):

    r.sadd("ips_sospechosas", ip)

    return {
        "mensaje": "IP agregada",
        "ip": ip
    }


@app.get("/ips")
def get_ips():

    ips = list(r.smembers("ips_sospechosas"))

    return {
        "ips_sospechosas": ips
    }