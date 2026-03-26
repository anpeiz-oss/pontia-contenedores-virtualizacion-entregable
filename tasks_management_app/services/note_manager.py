"""
1. Limpiar ciertas palabras malsonantes del contenido de una nota,
2. Hacer diferentes comprobaciones sobre la fecha deadline de la nota
"""

class NoteManager():
    def __init__(self):
        self.db = tasks_db.SessionLocal()
        tasks_db.createAllMetadata()

    def descartar_tareas_caducadas_mas_de_un_mes(self) -> int:
        # Obtener la fecha actual
        fecha_actual = datetime.now()
        # Obtener la fecha de hace un mes
        fecha_hace_un_mes = fecha_actual - timedelta(days=30)
        # Obtener todas las tareas
        # TODO importar correctamente el manejo de operaciones de repositorio, este código no es funcional.
        tareas = self.db.query(Task).all()
        # Filtrar las tareas que están caducadas y tienen más de un mes
        tareas_caducadas = [tarea for tarea in tareas if tarea.deadline < fecha_hace_un_mes]
        # Eliminar las tareas caducadas
        for tarea in tareas_caducadas:
            self.db.delete(tarea)
        # Guardar los cambios
        self.db.commit()
        # Devolver el número de tareas eliminadas
        return len(tareas_caducadas)
