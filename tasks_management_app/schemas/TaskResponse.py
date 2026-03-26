from pydantic import BaseModel, Field
from datetime import datetime, date

# Modelos Pydantic
class TaskResponse(BaseModel):
    id: int = Field(..., description="Identificador único de la tarea que genera el motor de base de datos.")
    titulo: str = Field(..., description="Título de la tarea.")
    contenido: str = Field(..., description="Contenido de la tarea.")
    deadline: date = Field(..., description="Fecha de vencimiento de la tarea.")
    completada: bool = Field(..., description="Estado que indica si la tarea está completada (true) o no (false).")
    fecha_creacion: datetime = Field(..., description="Fecha de creación de la tarea.")
