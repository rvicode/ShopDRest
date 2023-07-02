from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


# Show profile
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('username', 'email', 'password1', 'password2')


# Change profile
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
