from django.contrib import admin
from .models import Company, Department

# Configuración básica para visualizar los modelos en el panel de administración
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')  # Campos a mostrar en el panel de admin
    search_fields = ('name',)  # Agrega un buscador para el campo 'name'

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'created_at', 'updated_at')  # Mostrar campos en admin
    search_fields = ('name', 'company__name')  # Buscador por nombre de departamento y empresa
    list_filter = ('company',)  # Filtro por empresa en el panel de administración
