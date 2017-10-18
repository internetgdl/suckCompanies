from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from . import models
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def company_new(request):
    data = json.loads(request.body)
    print(data)
    company = models.Company(
        name = data["name"],
        complain = data["complain"],
        category = data["category"]
    )
    company.save();
    return HttpResponse(company)

def company_search(request):
    filterSearch = json.loads(request.body)
    result = models.Company.objects.get(name__contains=filterSearch.name)
    return HttpResponse(result)