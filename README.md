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
pip install -r requirements.txt
```

### 3. Ejecutar la aplicación

Puedes usar cualquiera de estos comandos:

```bash
# Opción 1: Comando moderno de FastAPI (recomendado)
fastapi dev .\tasks_management_app\main.py

# Opción 2: Uvicorn tradicional
uvicorn tasks_management_app.main:app --reload
```

La API estará disponible en `http://localhost:8000`

## Endpoints

### TODO: Documentar todos los endpoints

- `GET /` - Información de la API
- `POST /tasks/` - Crear una nueva tarea
- `GET /tasks/` - Obtener lista de todas las tareas
- `GET /tasks/caducadas` - Obtener lista de tareas caducadas
- `GET /tasks/activas` - Obtener lista de tareas activas
- `GET /tasks/completadas` - Obtener lista de tareas completadas
- `GET /tasks/{task_id}` - Obtener una tarea por ID
- `PUT /tasks/{task_id}/completar` - Marcar una tarea como completada
- `DELETE /tasks/{task_id}` - Eliminar una tarea por ID

## Ejecutar tests

```bash
python clients_task_management_app/test_api.py
```

## Documentación interactiva

Una vez ejecutando la aplicación, puedes acceder a:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
