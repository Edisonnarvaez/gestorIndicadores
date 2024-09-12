from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Role

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)  # Campos que quieres que aparezcan en el formulario de creación

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)  # Campos que quieres que aparezcan en el formulario de cambio

class UserAdmin(DefaultUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'is_staff', 'is_active')  # Campos a mostrar en la lista
    search_fields = ('email',)  # Campos a buscar en la administración
    ordering = ('email',)

    # Opcional: Configura el formulario para agregar usuarios
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
    )

    # Opcional: Configura el formulario para cambiar usuarios
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Role)
