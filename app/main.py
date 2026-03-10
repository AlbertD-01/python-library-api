from fastapi import FastAPI
from libro import Libro

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Fase 2 completada: Gestión de libro lista"}

@app.post("/libros/")
async def crear_libro(libro: Libro):
    return {"mensaje": "Libro recibido", "datos": libro}