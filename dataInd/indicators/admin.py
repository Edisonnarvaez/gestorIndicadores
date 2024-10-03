from django.contrib import admin

from .models.indicator import Indicator
from .models.macroprocess import MacroProcess
from .models.process import Process
from .models.result import Result
from .models.subprocess import SubProcess


@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('indicatorId', 'name', 'code', 'version', 'status', 'creationDate', 'updateDate')
    search_fields = ('name', 'code')
    list_filter = ('status', 'creationDate', 'updateDate')
    ordering = ('creationDate',)

@admin.register(MacroProcess)
class MacroProcessAdmin(admin.ModelAdmin):
    list_display = ('macroProcessId', 'name', 'code', 'version', 'status', 'creationDate', 'updateDate')
    search_fields = ('name', 'code')
    list_filter = ('status', 'creationDate', 'updateDate')
    ordering = ('creationDate',)

@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('processId', 'name', 'code', 'version', 'status', 'creationDate', 'updateDate')
    search_fields = ('name', 'code')
    list_filter = ('status', 'creationDate', 'updateDate')
    ordering = ('creationDate',)

@admin.register(SubProcess)
class SubProcessAdmin(admin.ModelAdmin):
    list_display = ('subProcessId', 'name', 'code', 'version', 'status', 'creationDate', 'updateDate')
    search_fields = ('name', 'code')
    list_filter = ('status', 'creationDate', 'updateDate')
    ordering = ('creationDate',)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('resultId', 'calculatedValue', 'numerator', 'denominator', 'creationDate', 'updateDate')
    search_fields = ('resultId',)
    list_filter = ('creationDate', 'updateDate')
    ordering = ('creationDate',)

