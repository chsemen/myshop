import os
from celery import Celery

# docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13.1-management
# celery -A myshop worker -l info - не работает
# https://celery.school/celery-on-windows
# celery -A myshop worker -l info -P gevent - работает, но требует gevent
# celery -A myshop worker -l info --pool=solo
# celery -A myshop worker -l info --pool=threads --concurrency=8

# Приложение для просмотра очереди
# celery -A myshop flower --basic-auth=user:pwd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app = Celery('myshop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()