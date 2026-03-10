from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {
        "status": "online",
        "message": "Servicio de Biblioteca funcionando correctamente",
        "fase": 1
    }
