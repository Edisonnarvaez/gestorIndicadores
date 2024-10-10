from django.contrib import admin

from .models.indicator import Indicator
from .models.macroprocess import MacroProcess
from .models.process import Process
from .models.result import Result
from .models.subprocess import SubProcess


@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'version', 'status', 'creationDate', 'updateDate')
    search_fields = ('name', 'code')
    list_filter = ('status', 'creationDate', 'updateDate')
    ordering = ('creationDate',)

@admin.register(MacroProcess)
class MacroProcessAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'version', 'status', 'creationDate', 'updateDate')
    search_fields = ('name', 'code')
    list_filter = ('status', 'creationDate', 'updateDate')
    ordering = ('creationDate',)

@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'version', 'status', 'creationDate', 'updateDate')
    search_fields = ('name', 'code')
    list_filter = ('status', 'creationDate', 'updateDate')
    ordering = ('creationDate',)

@admin.register(SubProcess)
class SubProcessAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'version', 'status', 'creationDate', 'updateDate')
    search_fields = ('name', 'code')
    list_filter = ('status', 'creationDate', 'updateDate')
    ordering = ('creationDate',)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'calculatedValue', 'numerator', 'denominator', 'creationDate', 'updateDate')
    search_fields = ('id',)
    list_filter = ('creationDate', 'updateDate')
    ordering = ('creationDate',)

