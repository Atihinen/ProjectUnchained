import json

from django.shortcuts import render
from models import Company
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse


def is_company_name_in_use(request, company_name):
    try:
        company = Company.objects.get(name=company_name)
    except ObjectDoesNotExist:
        company = None
 
    if company:
        response_data = _json_wrapper(409, "Company name already exists")
    else:
        response_data = _json_wrapper(200, "Company name is available")
    
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def _json_wrapper(status, msg):
    return {'status': status, 'msg': msg}