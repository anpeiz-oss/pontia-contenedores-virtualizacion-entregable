from fastapi import HTTPException
from models.task import Task
from repositories.task_repository import TaskRepository
from schemas.TaskCreate import TaskCreate

task_repository = TaskRepository()

class TaskService:
  
    def addTask(self, task: TaskCreate):
        if task_repository.checkIfTaskExists(task.titulo, task.deadline):
            raise HTTPException(
                status_code=400,
                detail=f"Ya existe una tarea con el mismo título '{task.titulo}' y la misma fecha de vencimiento '{task.deadline}'"
            )
        task_db = Task(**task.model_dump())
        task_created = task_repository.createTask(task_db)
        if task_created:
            return {
                "id": task_created.id,
                "titulo": task_created.titulo,
                "contenido": task_created.contenido,
                "deadline": task_created.deadline,
                "completada": task_created.completada,
                "fecha_creacion": task_created.fecha_creacion
            }
        else:
            raise HTTPException(
                status_code=500,
                detail="Error al crear la tarea"
            )
    
    def getTask(self, task_id: int):
        retrieved_task = task_repository.getTask(task_id)
        if retrieved_task is None:
            raise HTTPException(
                status_code=404,
                detail=f"No se encontró ninguna tarea con el id {task_id}"
            )
        return {
            "id": retrieved_task.id,
            "titulo": retrieved_task.titulo,
            "contenido": retrieved_task.contenido,
            "deadline": retrieved_task.deadline,
            "completada": retrieved_task.completada,
            "fecha_creacion": retrieved_task.fecha_creacion
        }
    
    def updateTask(self, task_id: int):
        updated_registers = task_repository.updateTask(task_id, True)
        if updated_registers == 0:
            raise HTTPException(
                status_code=404,
                detail=f"No se encontró ninguna tarea con el id {task_id}"
            )
        retrieved_task = task_repository.getTask(task_id)
        return {
            "id": retrieved_task.id,
            "titulo": retrieved_task.titulo,
            "contenido": retrieved_task.contenido,
            "deadline": retrieved_task.deadline,
            "completada": retrieved_task.completada,
            "fecha_creacion": retrieved_task.fecha_creacion
        }
    
    def deleteTask(self, task_id: int):
        deleted_registers = task_repository.deleteTask(task_id)
        if deleted_registers == 0:
            raise HTTPException(
                status_code=404,
                detail=f"No se encontró ninguna tarea con el id {task_id}"
            )
        return {"message": f"Tarea con el id {task_id} eliminada correctamente"}
    
    def getAllTasks(self):
        alltasks = task_repository.getAllTasks()
        return [
            {
                "id": task.id,
                "titulo": task.titulo,
                "contenido": task.contenido,
                "deadline": task.deadline,
                "completada": task.completada,
                "fecha_creacion": task.fecha_creacion
            }
            for task in alltasks
        ]

    def getActiveTasks(self):
        activetasks = task_repository.getActiveTasks()
        return [
            {
                "id": task.id,
                "titulo": task.titulo,
                "contenido": task.contenido,
                "deadline": task.deadline,
                "completada": task.completada,
                "fecha_creacion": task.fecha_creacion
            }
            for task in activetasks
        ]

    def getCompletedTasks(self):
        completedtasks = task_repository.getCompletedTasks()
        return [
            {
                "id": task.id,
                "titulo": task.titulo,
                "contenido": task.contenido,
                "deadline": task.deadline,
                "completada": task.completada,
                "fecha_creacion": task.fecha_creacion
            }
            for task in completedtasks
        ]
    
    def getExpiredTasks(self):
        expiredtasks = task_repository.getExpiredTasks()
        return [
            {
                "id": task.id,
                "titulo": task.titulo,
                "contenido": task.contenido,
                "deadline": task.deadline,
                "completada": task.completada,
                "fecha_creacion": task.fecha_creacion
            }
            for task in expiredtasks
        ]
