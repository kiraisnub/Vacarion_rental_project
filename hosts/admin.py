from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomHostUser
from .forms import CustomHostUserChangeForm,CustomHostUserCreationForm

# # Register your models here.
#
class CustomHostUserAdmin(UserAdmin):
    add_form = CustomHostUserCreationForm
    form = CustomHostUserChangeForm
    model=CustomHostUser
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'Profile', 'City')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name','last_name','email','password1', 'password2', 'Profile','City'),
        }),
    )
    list_display = ["username","email","first_name","City","Profile"]
#
admin.site.register(CustomHostUser,CustomHostUserAdmin)
