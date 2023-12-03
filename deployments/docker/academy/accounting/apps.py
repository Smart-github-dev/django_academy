from django.apps import AppConfig


class AccountingConfig(AppConfig):
    name = 'accounting'


    def ready(self):
        from accounting import hooks
        pass
