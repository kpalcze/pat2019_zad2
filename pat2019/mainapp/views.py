from django.shortcuts import render
from django.http import HttpResponse


from django.http import HttpResponse
from django.template import loader

from .models import Salary

def index(request):
    template = loader.get_template('mainapp/index.html')
    return HttpResponse(template.render({}, request))


def raw_data(request):
    salary_list = Salary.objects.all()
    template = loader.get_template('mainapp/data_table.html')
    context = {
        'salary_list': salary_list,
    }
    return HttpResponse(template.render(context, request))


def predicted_data(request):
    salary_list = Salary.objects.all()
    template = loader.get_template('mainapp/data_table.html')
    context = {
        'salary_list': salary_list,
    }
    return HttpResponse(template.render(context, request))
