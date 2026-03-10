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

    def devolver_libro(self, titulo: str):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                if not libro.disponible:
                    libro.disponible = True
                    return {"exito": True, "mensaje": f"Libro '{libro.titulo}' devuelto correctamente."}
                else:
                    return {"exito": False, "mensaje": f"El libro '{libro.titulo}' ya estaba disponible."}

        return {"exito": False, "mensaje": "Libro no encontrado en el sistema."}

    def obtener_estadisticas(self):
        total = len(self.libros)
        disponibles = len([libro for libro in self.libros if libro.disponible])
        prestados = total - disponibles

        return {
            "total_libros": total,
            "libros_disponibles": disponibles,
            "libros_prestados": prestados
        }