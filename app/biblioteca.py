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
