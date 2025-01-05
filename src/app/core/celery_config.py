from celery import Celery

# Create Celery instance
celery_app = Celery(
    'tasks',
    result_backend='redis://172.18.0.3:6379/0',  # Correct IP address for Redis
    broker='redis://172.18.0.3:6379/0'  # Correct IP address for Redis
)

# Celery configuration settings (optional)
celery_app.conf.update(
    result_expires=3600,
    task_serializer='json',
    # Make sure result_backend is not overridden with localhost
)
