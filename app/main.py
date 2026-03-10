from fastapi import FastAPI
from app.libro import Libro
from app.biblioteca import Biblioteca

app = FastAPI()

mi_biblioteca = Biblioteca()

@app.get("/")
async def root():
    return {"mensaje": "API de Biblioteca lista"}

@app.get("/libros")
async def obtener_catalogo():
    return mi_biblioteca.consultar_libros()