
from fastapi import FastAPI
from pydantic import BaseModel, Field

# Creamos nuestra aplicación FastAPI.
app = FastAPI()


# Endpoint para consultar el mensaje de bienvenida.
@app.get("/")
def inicio():
    return {"message": "Bienvenido a SprintBoard"}


# Modelo Pydantic: define los datos necesarios
# para crear una tarea y sus validaciones.
class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    description: str = ""


# Lista temporal donde guardaremos las tareas.
tasks = []


# Endpoint POST /tasks para crear una tarea.
@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):

    # Construimos un diccionario con la nueva tarea.
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "description": task.description,
        "completed": False
    }

    # Guardamos la tarea en memoria.
    tasks.append(new_task)

    # FastAPI convierte el resultado en una respuesta JSON.
    return new_task
