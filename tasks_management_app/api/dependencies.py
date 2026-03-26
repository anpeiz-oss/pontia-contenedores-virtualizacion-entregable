def get_task_service():
    """Provides a TaskService instance via dependency injection."""
    from services.task_service import TaskService
    return TaskService()
