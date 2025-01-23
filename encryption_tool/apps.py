from django.apps import AppConfig

class EncryptionToolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'encryption_tool'

def ready(self):
    import encryption_tool.signals
