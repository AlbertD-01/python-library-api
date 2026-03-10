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

@app.post("/libros", status_code=201)
async def crear_libro(nuevo_libro: Libro):
    mensaje = mi_biblioteca.agregar_libro(nuevo_libro)
    return {
        "status": "success",
        "message": mensaje,
        "libro_guardado": nuevo_libro
    }

@app.get("/libros/buscar")
async def buscar_libro_por_titulo(titulo: str):
    return mi_biblioteca.buscar_por_titulo(titulo)


@app.post("/libros/prestar")
async def prestar_libro(titulo: str):
    resultado = mi_biblioteca.prestar_libro(titulo)

    return resultado 