from pydantic import BaseModel, Field

# Modelos Pydantic
class TaskUpdate(BaseModel):
    completada: bool = Field(..., default=False, description="Estado que indica si la tarea está completada (true) o no (false).")
