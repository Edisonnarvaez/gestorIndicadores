from django.contrib import admin
from .models import Indicator, Process, SubProcess, Result

# Registro del modelo Indicator
@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'process', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('process',)

# Registro del modelo Process
@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('name', 'macroprocess', 'created_at', 'updated_at')
    search_fields = ('name', 'macroprocess__name')
    list_filter = ('macroprocess',)

# Registro del modelo SubProcess
@admin.register(SubProcess)
class SubProcessAdmin(admin.ModelAdmin):
    list_display = ('name', 'process', 'created_at', 'updated_at')
    search_fields = ('name', 'process__name')
    list_filter = ('process',)

# Registro del modelo Result
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('indicator', 'value', 'date', 'created_at', 'updated_at')
    search_fields = ('indicator__name', 'value')
    list_filter = ('indicator', 'date')

