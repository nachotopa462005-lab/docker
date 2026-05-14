from fastapi import FastAPI

app = FastAPI()

inventario = [
    {"id": 1, "producto": "Teclado", "stock": 10},
    {"id": 2, "producto": "Mouse", "stock": 5}
]

@app.get("/status")
def status():
    return {"estado": "API funcifuncionando de lujo"}

@app.get("/inventario")
def inventario_endpoint():
    return inventario