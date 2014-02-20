from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def register(request):
    return render(request, 'register/register.html')

def do_register(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_user(username, email, password)
    if user:
        user.is_active = true
        user.save()
        messages.add_message(request, messages.ERROR, 'Your account has been registered and activated')
        return redirect('/')
    else:
        messages.add_message(request, messages.ERROR, 'Register failed')
        return redirect('/accounts/register')
