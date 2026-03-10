from typing import List
from app.libro import Libro
class Biblioteca:
    def __init__(self):
        self.libros: List[Libro] = []

    def agregar_libro(self, libro: Libro):
        self.libros.append(libro)
        return f"Libro '{libro.titulo}' agregado correctamente."

    def consultar_libros(self):
        return self.libros

    def buscar_por_titulo(self, titulo: str):
        resultados = [
            libro for libro in self.libros
            if titulo.lower() in libro.titulo.lower()
        ]
        return resultados

    def prestar_libro(self, titulo: str):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                if libro.disponible:
                    libro.disponible = False
                    return {"exito": True, "mensaje": f"Libro '{libro.titulo}' prestado con éxito."}
                else:
                    return {"exito": False, "mensaje": f"El libro '{libro.titulo}' ya está prestado."}

        return {"exito": False, "mensaje": "Libro no encontrado."}