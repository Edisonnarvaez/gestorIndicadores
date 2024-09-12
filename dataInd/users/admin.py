from django.contrib import admin
from .models.user import User
from .models.role import Role

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('userId', 'firstName', 'lastName', 'username', 'email', 'phone', 'status', 'companyId', 'departmentId', 'role', 'creationDate', 'lastLogin')
    search_fields = ('username', 'firstName', 'lastName', 'email')
    list_filter = ('status', 'companyId', 'departmentId', 'role')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('roleId', 'name', 'description')
    search_fields = ('name',)

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import User, Role

# class UserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('email',)  # Campos que quieres que aparezcan en el formulario de creación

# class UserChangeForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ('email',)  # Campos que quieres que aparezcan en el formulario de cambio

# class UserAdmin(DefaultUserAdmin):
#     form = UserChangeForm
#     add_form = UserCreationForm
#     list_display = ('email', 'is_staff', 'is_active')  # Campos a mostrar en la lista
#     search_fields = ('email',)  # Campos a buscar en la administración
#     ordering = ('email',)

#     # Opcional: Configura el formulario para agregar usuarios
#     add_fieldsets = (
#         (None, {'fields': ('email', 'password1', 'password2')}),
#     )

#     # Opcional: Configura el formulario para cambiar usuarios
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )

# admin.site.register(User, UserAdmin)
# admin.site.register(Role)