from fastapi import FastAPI
from libro import Libro
from biblioteca import Biblioteca

app = FastAPI(title="Mi API de Biblioteca")

mi_biblioteca = Biblioteca()

@app.get("/libros/")
async def listar_libros():
    return mi_biblioteca.consultar_libros()

@app.post("/libros/")
async def añadir_libro(libro: Libro):
    mensaje = mi_biblioteca.agregar_libro(libro)
    return {"status": "success", "message": mensaje}