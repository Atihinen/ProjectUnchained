from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render_to_response('index.html', context_instance = RequestContext(request))