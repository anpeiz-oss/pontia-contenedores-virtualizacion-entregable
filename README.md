# Task Management API

API REST para la gestión de tareas desarrollada con FastAPI.

## Instalación

### 1. Crear entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r ./tasks_management_app/requirements.txt
```

### 3. Ejecutar la aplicación

Puedes usar este comando:

```bash
fastapi dev .\tasks_management_app\main.py

```

La API estará disponible mediante el puerto 8080 en un contenedor docker accesible desde el host sobre el que se ejecuta el docker engine y para el caso de un equipo local la encontontraremos en `http://localhost:8080`

## Endpoints

### Endpoints RESTFUL expuestos

- `GET /` - Información de la API
- `POST /tasks/` - Crear una nueva tarea
- `PATCH /tasks/{task_id}` - Actualiza una tarea existente
- `PUT /tasks/{task_id}/completar` - Marcar una tarea como completada
- `GET /tasks/` - Obtener lista de todas las tareas
- `GET /tasks/caducadas` - Obtener lista de tareas caducadas
- `GET /tasks/activas` - Obtener lista de tareas activas
- `GET /tasks/completadas` - Obtener lista de tareas completadas
- `GET /tasks/{task_id}` - Obtener una tarea por ID
- `DELETE /tasks/{task_id}` - Eliminar una tarea por ID

## Ejecutar tests

```bash
python clients_task_management_app/test_api.py
```

## Documentación interactiva

Una vez ejecutando la aplicación, puedes acceder a:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
