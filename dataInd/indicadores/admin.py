from .models import Company, Role, Department, User, MacroProcess, Process, SubProcess, Indicator, Result
from django.contrib import admin

# Registro de cada modelo en el panel de administración
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('companyId', 'name', 'nit', 'legalRepresentative', 'phone', 'status')
    search_fields = ('name', 'nit', 'legalRepresentative')
    list_filter = ('status',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('roleId', 'name')
    search_fields = ('name',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('departmentId', 'name', 'departmentCode', 'companyId', 'status')
    search_fields = ('name', 'departmentCode')
    list_filter = ('status',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('userId', 'username', 'firstName', 'lastName', 'email', 'companyId', 'role', 'status')
    search_fields = ('username', 'email', 'firstName', 'lastName')
    list_filter = ('status', 'role', 'companyId')

@admin.register(MacroProcess)
class MacroProcessAdmin(admin.ModelAdmin):
    list_display = ('macroProcessId', 'name', 'departmentId', 'code', 'version', 'status')
    search_fields = ('name', 'code', 'version')
    list_filter = ('status', 'departmentId')

@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('processId', 'name', 'macroProcessId', 'code', 'version', 'status')
    search_fields = ('name', 'code', 'version')
    list_filter = ('status', 'macroProcessId')

@admin.register(SubProcess)
class SubProcessAdmin(admin.ModelAdmin):
    list_display = ('subProcessId', 'name', 'processId', 'code', 'version', 'status')
    search_fields = ('name', 'code', 'version')
    list_filter = ('status', 'processId')

@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('indicatorId', 'name', 'subProcessId', 'code', 'version', 'target', 'status')
    search_fields = ('name', 'code', 'version', 'target')
    list_filter = ('status', 'subProcessId')

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('resultId', 'numerator', 'denominator', 'calculatedValue', 'indicatorId', 'creationDate')
    search_fields = ('indicatorId__name',)
    list_filter = ('creationDate',)

