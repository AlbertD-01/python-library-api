# python-library-api
Biblioteca hecha en python con FastAPI implementado 


🛠️ 1. Configuración del Entorno

Para replicar este proyecto desde cero:

    Crear entorno virtual: python -m venv .venv

    Activar entorno: source .venv/bin/activate (Linux/Mac) o .venv\Scripts\activate (Windows).

    Instalar dependencias: pip install "fastapi[standard]"

📂 2. Estructura del Proyecto

La organización de archivos sigue el principio de Separación de Responsabilidades:
Plaintext

python-library-api/
├── .venv/               # Entorno virtual
├── README.md            # Documentación
└── app/                 # Carpeta principal del código
    ├── __init__.py      # (Opcional) Indica que es un paquete
    ├── main.py          # Servidor y Endpoints (FastAPI)
    ├── libro.py         # Modelo de datos (Pydantic)
    └── biblioteca.py    # Lógica de negocio (Clase Biblioteca)

💻 3. El Código Final
A. Modelo de Datos (app/libro.py)

Define la estructura de un libro y valida los tipos de datos.
Python

from pydantic import BaseModel

class Libro(BaseModel):
    titulo: str
    autor: str
    anio: int
    disponible: bool = True  # Valor por defecto

B. Lógica de Negocio (app/biblioteca.py)

Gestiona la lista de libros en memoria y las operaciones de búsqueda y préstamo.
Python

from typing import List
from libro import Libro  # Importación local para ejecución desde /app

class Biblioteca:
    def __init__(self):
        self.libros: List[Libro] = []

    def agregar_libro(self, libro: Libro):
        self.libros.append(libro)
        return f"Libro '{libro.titulo}' agregado."

    def consultar_libros(self):
        return self.libros

    def buscar_por_titulo(self, titulo: str):
        return [l for l in self.libros if titulo.lower() in l.titulo.lower()]

    def prestar_libro(self, titulo: str):
        for l in self.libros:
            if l.titulo.lower() == titulo.lower() and l.disponible:
                l.disponible = False
                return {"exito": True, "msj": "Prestado"}
        return {"exito": False, "msj": "No disponible o no encontrado"}

    def devolver_libro(self, titulo: str):
        for l in self.libros:
            if l.titulo.lower() == titulo.lower() and not l.disponible:
                l.disponible = True
                return {"exito": True, "msj": "Devuelto"}
        return {"exito": False, "msj": "Ya estaba disponible o no encontrado"}

    def obtener_estadisticas(self):
        total = len(self.libros)
        disponibles = len([l for l in self.libros if l.disponible])
        return {
            "total": total,
            "disponibles": disponibles,
            "prestados": total - disponibles
        }

C. Servidor API (app/main.py)

Punto de entrada que conecta las peticiones HTTP con la lógica de la biblioteca.
Python

from fastapi import FastAPI
from libro import Libro
from biblioteca import Biblioteca

app = FastAPI(title="Mi Biblioteca API")
mi_biblioteca = Biblioteca()

@app.get("/")
def home():
    return {"status": "Online"}

@app.get("/libros")
def listar():
    return mi_biblioteca.consultar_libros()

@app.post("/libros", status_code=201)
def crear(libro: Libro):
    return mi_biblioteca.agregar_libro(libro)

@app.get("/libros/buscar")
def buscar(titulo: str):
    return mi_biblioteca.buscar_por_titulo(titulo)

@app.post("/libros/prestar")
def prestar(titulo: str):
    return mi_biblioteca.prestar_libro(titulo)

@app.post("/libros/devolver")
def devolver(titulo: str):
    return mi_biblioteca.devolver_libro(titulo)

@app.get("/estadisticas")
def estadisticas():
    return mi_biblioteca.obtener_estadisticas()

🐙 4. Flujo de Trabajo con Git

Para cada fase, seguimos este protocolo profesional:

    Crear Rama: git checkout -b feature/nombre-fase

    Desarrollar: Escribir código y probar en /docs.

    Commit: git add . -> git commit -m "feat: descripción del cambio"

    Push: git push origin feature/nombre-fase

    Merge: Realizar Pull Request en la web y fusionar a main.

    Sincronizar: git checkout main -> git pull origin main

🚀 5. Ejecución y Pruebas

Para poner en marcha la API, sitúate en la carpeta python-library-api y ejecuta:
Bash

uvicorn app.main:app --reload

    Documentación Interactiva: http://127.0.0.1:8000/docs

    Probar POST: Usa el JSON de ejemplo para crear libros.

    Probar Persistencia: Recuerda que al reiniciar el servidor (o guardar cambios), los datos en memoria se borran.
