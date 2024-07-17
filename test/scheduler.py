from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings

def start():
    if settings.DEBUG:
        from .views import test
        scheduler = BackgroundScheduler()
        scheduler.add_job(test, 'interval', minutes=5)
        scheduler.start()
