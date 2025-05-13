from django.apps import AppConfig


class CompaniesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'companies'
    verbose_name = 'Gestión de Empresas y Areas'  # Nombre legible en el panel de admin
