import os

from celery import Celery

celery_app = Celery('tasks', broker=os.environ.get('AMQP_URL'), backend=os.environ.get('DATABASE_URL'))