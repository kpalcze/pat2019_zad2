from django.db import models


class Salary(models.Model):
    workedYears = models.CharField(max_length=200, default=' ')
    salaryBrutto = models.CharField(max_length=200, default=' ')


class SalaryPredicted(models.Model):
    workedYears = models.FloatField(null=True)
    salaryBrutto = models.FloatField(null=True)
    salaryBruttoPredicted = models.FloatField(null=True)

