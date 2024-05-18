# apps.py
from django.apps import AppConfig

class TaskMgmtConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'taskMgmt'

    def ready(self):
        import taskMgmt.signals
