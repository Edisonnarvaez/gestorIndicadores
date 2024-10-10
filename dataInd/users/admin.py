from django.contrib import admin
from .models.user import User
from .models.role import Role

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstName', 'lastName', 'username', 'email', 'phone', 'status', 'company', 'department', 'role', 'creationDate', 'lastLogin')
    search_fields = ('username', 'firstName', 'lastName', 'email')
    list_filter = ('status', 'company', 'department', 'role')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)

