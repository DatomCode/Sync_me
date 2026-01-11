from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser


# To create the user
class CreateUser(UserCreationForm):
    class Meta:

        model = CustomUser
        fields = ("username", "email")


# To be alle to edit user information
class EditUser(UserChangeForm):
    class Meta:

        model = CustomUser
        fields = ("username", "email")
