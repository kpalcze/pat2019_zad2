from jchart import Chart
from jchart.config import DataSet
import numpy as np

from ..models import SalaryPredicted

def getHistogram():
    salary_list = SalaryPredicted.objects.all()
    data = []
    for salary in salary_list:
        if salary.salaryBrutto is None:
            data.append(salary.salaryBruttoPredicted)
        else:
            data.append(salary.salaryBrutto)
    return np.histogram(data)

class ScatterChart(Chart):
    chart_type = 'scatter'

    def get_datasets(self, **kwargs):
        salary_list = SalaryPredicted.objects.all()
        data = []
        for salary in salary_list:
            if salary.salaryBrutto is None:
                data.append({'x': salary.workedYears, 'y': salary.salaryBruttoPredicted})
            else:
                data.append({'x': salary.workedYears, 'y': salary.salaryBrutto})
        return [DataSet(data=data, label="Salary")]

class PieChart(Chart):
        chart_type = 'pie'

        def get_datasets(self, **kwargs):
            return [DataSet(data=getHistogram()[0].tolist())]

        def get_labels(self, **kwargs):
            return getHistogram()[1].tolist()
