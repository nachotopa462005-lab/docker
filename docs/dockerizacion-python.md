# Dockerización de Python con fast API

## 1. API REST con FastAPI

Para este proyecto se creó una pequeña API REST utilizando FastAPI, que expone dos endpoints principales:

- `/status`: devuelve el estado de la API
- `/inventario`: devuelve una lista de productos en inventario

Ejemplo de código:

```python
from fastapi import FastAPI

app = FastAPI()

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