from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/inventario")
async def inventario():
    await asyncio.sleep(3)
    return {"mensaje": "Inventario OK"}

@app.get("/pagos")
async def pagos():
    await asyncio.sleep(3)
    return {"mensaje": "Pagos OK"}

@app.get("/usuarios")
async def usuarios():
    await asyncio.sleep(3)
    return {"mensaje": "Usuarios OK"}

@app.get("/notificaciones")
async def notificaciones():
    await asyncio.sleep(3)
    return {"mensaje": "Notificaciones OK"}