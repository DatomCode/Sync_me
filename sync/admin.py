from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ["username", "email"]

admin.site.register(CustomUser, CustomUserAdmin)