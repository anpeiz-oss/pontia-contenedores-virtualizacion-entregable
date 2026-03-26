from api.dependencies import get_task_service
from fastapi import Depends
from fastapi import APIRouter, status
from schemas.TaskCreate import TaskCreate
from schemas.TaskResponse import TaskResponse
from services.task_service import TaskService
from typing import List

import logging

# --- Logging ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def crear_tarea(task: TaskCreate, task_service: TaskService = Depends(get_task_service)):
    logger.info(f"Recibida petición de creación de tarea con el siguiente cuerpo: {task}")
    return task_service.addTask(task)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_tarea(task_id: int, task_service: TaskService = Depends(get_task_service)):
    logger.info(f"Recibida petición de eliminación de tarea con el siguiente id: {task_id}")
    task_service.deleteTask(task_id)

@router.patch("/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def actualizar_tarea(task_id: int, task: TaskCreate, task_service: TaskService = Depends(get_task_service)):
    logger.info(f"Recibida petición de actualización de tarea con el siguiente id: {task_id} y el siguiente cuerpo: \n{task}")
    return task_service.updateTask(task_id, task)

@router.put("/{task_id}/completar", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def marcar_completada(task_id: int, task_service: TaskService = Depends(get_task_service)):
    logger.info(f"Recibida petición de completado de tarea con el siguiente id: {task_id}")
    return task_service.completeTask(task_id)

@router.get("/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def obtener_tarea(task_id: int, task_service: TaskService = Depends(get_task_service)):
    logger.info(f"Recibida petición de obtención de tarea con el siguiente id: {task_id}")
    return task_service.getTask(task_id)

@router.get("/", response_model=List[TaskResponse], status_code=status.HTTP_200_OK)
def obtener_todas_tareas(task_service: TaskService = Depends(get_task_service)):
    logger.info("Recibida petición de obtención de todas las tareas")
    return task_service.getAllTasks()

@router.get("/activas/", response_model=List[TaskResponse], status_code=status.HTTP_200_OK)
def obtener_tareas_activas(task_service: TaskService = Depends(get_task_service)):
    logger.info("Recibida petición de obtención de tareas activas")
    return task_service.getActiveTasks()

@router.get("/caducadas/", response_model=List[TaskResponse], status_code=status.HTTP_200_OK)
def obtener_tareas_caducadas(task_service: TaskService = Depends(get_task_service)):
    logger.info("Recibida petición de obtención de tareas caducadas")
    return task_service.getExpiredTasks()

@router.get("/completadas/", response_model=List[TaskResponse], status_code=status.HTTP_200_OK)
def obtener_tareas_completadas(task_service: TaskService = Depends(get_task_service)):
    logger.info("Recibida petición de obtención de tareas completadas")
    return task_service.getCompletedTasks()  
