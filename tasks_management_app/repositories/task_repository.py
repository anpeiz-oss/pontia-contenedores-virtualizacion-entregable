from database.session import get_session
from models.task import Task
from datetime import date
import logging

# --- Logging ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class TaskRepository:

    def checkIfTaskExists(self, titulo: str, deadline: date) -> bool:
        with get_session() as session:
            existing = session.query(Task).filter(
                Task.titulo == titulo,
                Task.deadline == deadline
            ).first()
            if existing is not None:
                logger.info(f"Registro recuperado de base de datos para validar si existe alguna con el mismo titulo y fecha de vencimiento: {existing.id}, {existing.titulo}, {existing.deadline}, {existing.completada}, {existing.fecha_creacion}")
            return existing is not None

    def createTask(self, task: Task):
        with get_session() as session:
            session.add(task)
            session.flush()
            session.refresh(task)
            return task

    def getTask(self, task_id: int):
        with get_session() as session:
            task = session.query(Task).filter(Task.id == task_id).first()
            if task is not None:
                logger.info(f"Registro recuperado de base de datos para obtener la tarea con el id: {task.id}, {task.titulo}, {task.deadline}, {task.completada}, {task.fecha_creacion}")
            return task

    def updateTask(self, task_id: int, completada: bool):
        with get_session() as session:
            updatedregisters = session.query(Task).filter(Task.id == task_id).update({Task.completada: completada})
            if updatedregisters > 0:
                logger.info(f"{updatedregisters} registros de tarea actualizados en base de datos asociados al id {task_id} con el valor completada a {completada}")
            return updatedregisters

    def deleteTask(self, task_id: int):
        with get_session() as session:
            deletedregisters = session.query(Task).filter(Task.id == task_id).delete()
            if deletedregisters > 0:
                logger.info(f"{deletedregisters} registros de tarea eliminados en base de datos asociados al id {task_id}")
            return deletedregisters

    def getAllTasks(self):
        with get_session() as session:
            alltasks = session.query(Task).all()
            if alltasks is not None:
                logger.info(f"{len(alltasks)} registros de tareas sin filtrar, recuperados de base de datos.")
            return alltasks

    def getActiveTasks(self):
        with get_session() as session:
            activetasks = session.query(Task).filter(Task.completada == False, Task.deadline > date.today()).all()
            if activetasks is not None:
                logger.info(f"{len(activetasks)} registros de tareas activas (no completadas ni expiradas), recuperados de base de datos.")
            return activetasks

    def getCompletedTasks(self):
        with get_session() as session:
            completedtasks = session.query(Task).filter(Task.completada == True).all()
            if completedtasks is not None:
                logger.info(f"{len(completedtasks)} registros de tareas completadas, recuperados de base de datos.")
            return completedtasks

    def getExpiredTasks(self):
        with get_session() as session:
            expiredtasks = session.query(Task).filter(Task.deadline <= date.today()).all()
            if expiredtasks is not None:
                logger.info(f"{len(expiredtasks)} registros de tareas expiradas, recuperados de base de datos.")
            return expiredtasks
