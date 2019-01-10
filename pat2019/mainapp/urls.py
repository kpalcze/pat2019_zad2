from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('raw_data', views.raw_data, name='raw_data'),
    path('predicted_data', views.predicted_data, name='predicted_data'),
    path('chart', views.chart, name='chart'),
]