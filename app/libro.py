from pydantic import BaseModel

class Libro(BaseModel):
    titulo: str
    autor: str
    anio: int
    disponible: bool = True
