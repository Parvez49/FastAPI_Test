from celery import Celery

def make_celery() -> Celery:
    celery = Celery(
        'fastapi_app',  # Name of your Celery app
        broker="redis://redis:6379/0",  # Redis broker URL
        backend="redis://redis:6379/0"   # Redis backend for results
    )
    return celery

celery = make_celery()


# @celery.task
# def some_long_task(data):
#     # Task logic here
#     return data

# @app.post("/long-task/")
# async def trigger_long_task(data: dict):
#     task = some_long_task.delay(data)  # Call Celery task
#     return {"task_id": task.id}
