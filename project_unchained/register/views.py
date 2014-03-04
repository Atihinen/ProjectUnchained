import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.db import IntegrityError
from gui.forms import RegisterForm
from gui.forms import CompanyRegistrationForm
from company.models import Company
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def index(request):
    if request.method == "POST":
        with_company = False
        form = RegisterForm(request.POST)
        company_form = CompanyRegistrationForm(request.POST)
        
        if request.POST["name"] and request.POST["name"] != "":
            with_company = True
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            try:
                user = User.objects.create_user(username, email, password)
            except IntegrityError as e:
                messages.add_message(request, messages.ERROR, "Username is already in use.")
                return redirect("/accounts/register")
            except ValueError:
                messages.add_message(request, messages.ERROR, "Fill required fields")
                return redirect("/accounts/register")
            
            if user:
                user.is_active = True
                user.save()
                if with_company:
                    if company_form.is_valid():
                        cname = company_form.cleaned_data['name']
                        cwww = company_form.cleaned_data['www']
                        cadmin = user
                        cpublic = company_form.cleaned_data['public']
                        company = Company.objects.create(name=cname, www=cwww, admin=cadmin, public=cpublic)
                        company.save()
                        messages.add_message(request, messages.SUCCESS, "Your comnpany %s has been registered." % cname)
                    else:
                        user.delete()
                        messages.add_message(request, messages.ERROR, "Fill optional fields")
                        data = {
                            'form': form,
                            'cform': company_form,
                        }
                        return render(request, 'register/register.html', data)
                messages.add_message(request, messages.SUCCESS, 'Your account has been registered and activated, please do login')
                authenticate(username=user.username, password=user.password)
                return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, 'Register failed')
                return redirect('/accounts/register')
        else:
            messages.add_message(request, messages.ERROR, 'Fill required fields')
            data = {
                'form': form,
                'cform': company_form,
            }
            return render(request, 'register/register.html', data)
            
    else:
        form = RegisterForm()
        company_form = CompanyRegistrationForm()
        data = {
            'form': form,
            'cform': company_form,
        }
        return render(request, 'register/register.html', data)
    

def is_username_in_use(request, username):
    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        user = None
 
    if user:
        response_data = _json_wrapper(409, "Username already exists")
    else:
        response_data = _json_wrapper(200, "Username is available")
    
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def is_email_in_use(request, email):
    user = User.objects.filter(email=email)
    if user:
        response_data = _json_wrapper(409, "Email already exists")
    else:
        response_data = _json_wrapper(200, "Email is available")
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def _json_wrapper(status, msg):
    return {'status': status, 'msg': msg}
