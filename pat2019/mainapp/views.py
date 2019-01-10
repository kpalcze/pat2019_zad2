from django.http import HttpResponse
from django.template import loader

from .charts.chart import ScatterChart, PieChart
from .models import Salary
from .machinelearning.linearregression import *
from .db.databasemanager import *


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
    predicted_salary = calculate_predicted_salary(Salary.objects.all())
    update_salary_predicted(predicted_salary)
    template = loader.get_template('mainapp/data_table_predicted.html')
    context = {
        'salary_list': SalaryPredicted.objects.all(),
    }
    return HttpResponse(template.render(context, request))


def chart(request):
    template = loader.get_template('mainapp/chart.html')
    context = {
        'chart': ScatterChart(),
        'pie_chart': PieChart()
    }
    return HttpResponse(template.render(context, request))
