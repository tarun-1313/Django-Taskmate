from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from .forms import CustomRegisterForm
# Create your views here.
def register(request):
    if request.method == "POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request ,"Registration Successful! Login to continue.")
            return redirect('register')
        else:
            return render(request, 'register.html', {'register_form': register_form})
    
    register_form = CustomRegisterForm()
    return render(request, 'register.html', {'register_form': register_form})
