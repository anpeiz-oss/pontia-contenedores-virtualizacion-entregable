from pydantic import BaseModel, Field, field_validator
from datetime import datetime, date

PALABRAS_PROHIBIDAS_ES = ["puto", "coño", "joder", "mierda", "hostia", "carajo", "cabron", "gilipollas", "pene", "vagina", "culo", "tetas", "zorra", "maricon"]

# Modelos Pydantic
class TaskCreate(BaseModel):
    titulo: str = Field(..., min_length=1, description="Título de la tarea.")
    contenido: str = Field(..., min_length=1, description="Contenido de la tarea.")
    deadline: date = Field(..., gt=date.today(), description="Fecha de vencimiento de la tarea.")
    completada: bool = Field(default=False, description="Estado que indica si la tarea está completada (true) o no (false).")
    fecha_creacion: datetime = Field(default=datetime.now(), description="Fecha de creación de la tarea.")

    @field_validator("contenido", mode="before")
    def limpiar_palabras_prohibidas(cls, value):
        for palabra in PALABRAS_PROHIBIDAS_ES:
            value = value.replace(palabra, "*")
        return value
