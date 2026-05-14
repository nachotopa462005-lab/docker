from fastapi import FastAPI
import json
import os

app = FastAPI()

FILE_PATH = "data/inventario.json"

os.makedirs("data", exist_ok=True)

if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w") as f:
        json.dump([], f)


@app.get("/status")
def status():
    return {"estado": "API funcionando"}


@app.get("/inventario")
def get_inventario():
    with open(FILE_PATH, "r") as f:
        return json.load(f)


@app.post("/inventario")
def add_item(item: dict):
    with open(FILE_PATH, "r") as f:
        data = json.load(f)

    data.append(item)

    with open(FILE_PATH, "w") as f:
        json.dump(data, f)

    return {"mensaje": "item agregado", "item": item}