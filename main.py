from fastapi import FastAPI
from app.controllers.task_controller import router as task_router

app = FastAPI()

app.include_router(task_router)

@app.get("/")
def inicio():
    return {"message": "Bienvenido a SprintBoard"}