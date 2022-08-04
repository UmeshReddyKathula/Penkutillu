from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUser(UserCreationForm):
    class Mata:
        model = User
        fields = ['username', 'email', 'password1', 'password2']