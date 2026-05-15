from fastapi import FastAPI
import redis
import os

app = FastAPI()

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = 6379
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "1234")

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


@app.get("/redis")
def redis_test():
    r.set("mensaje", "Redis funcionando")
    return {"redis": r.get("mensaje")}