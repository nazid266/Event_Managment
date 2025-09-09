from django.apps import AppConfig


class EventUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'event_users'
    
    def ready(self):
        import event_users.signals
