from django.contrib import admin
from .models.company import Company
from .models.department import Department

# Configurar el modelo Company en el admin
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('companyId', 'name', 'nit', 'status')
    search_fields = ('companyId', 'name', 'nit')
    list_filter = ('status',)
    ordering = ('companyId',)

# Configurar el modelo Department en el admin
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('departmentId', 'name', 'companyId', 'status')
    search_fields = ('departmentId', 'name', 'companyId__name')
    list_filter = ('status',)
    ordering = ('departmentId',)
