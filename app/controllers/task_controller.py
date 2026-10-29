from fastapi import APIRouter
from app.schemas.task import TaskCreate

# Creamos un router para los endpoints de tareas.
router = APIRouter()

# Almacenamiento temporal de tareas.
tasks = []

@router.post("/tasks", status_code=201)
def create_task(task: TaskCreate):

    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "description": task.description,
        "completed": False
    }

    tasks.append(new_task)
    return new_task