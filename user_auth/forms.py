from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# create the registration form class

"""
This class adds more fiels to the built-in user registration form
"""
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        if commit:
            user.save()
        return user









