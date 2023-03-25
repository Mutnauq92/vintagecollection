from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# views
def register_user(request):
    if request.method == 'POST':
        # UserRegistrationForm adds an extra field to the built-in form fields, 'first_name'
        # as it is not available by default in Django
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save() # save the user information from filled form
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            password = form.cleaned_data['password1']  # using the first password entered in the form
            user = authenticate(username=username, password=password, first_name=first_name)
            login(request, user) # automatically login the user

            # return redirect(request, 'polls:index')
            return HttpResponseRedirect(reverse('user_auth:homepage'))
    else:
        form = UserRegistrationForm()

    return render(request, 'authentication/register.html', {
        'form': form,
    })
    
def user_login(request):
    return render(request, 'authentication/login.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_auth:homepage'))

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    
    if user is None:
        return HttpResponseRedirect(
        reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('user_auth:homepage'))
        
def homepage(request):
    return redirect("gallery:gallery")








