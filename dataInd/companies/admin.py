from django.contrib import admin
from .models.company import Company
from .models.department import Department

# Configurar el modelo Company en el admin
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'nit', 'status')
    search_fields = ('name', 'nit')
    list_filter = ('status',)
    ordering = ('id',)

# Configurar el modelo Department en el admin
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company', 'status')
    search_fields = ('name', 'companyId__name')
    list_filter = ('status',)
    ordering = ('id',)

