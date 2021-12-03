from scheduler_config import config
from main import Task
from gpu_task_scheduler.gpu_task_scheduler import GPUTaskScheduler

scheduler = GPUTaskScheduler(config=config, gpu_task_class = Task)
scheduler.start()
