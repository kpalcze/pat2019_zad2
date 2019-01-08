from django.db import models


class Salary(models.Model):
    workedYears = models.CharField(max_length=200, default=' ')
    salaryBrutto = models.CharField(max_length=200, default=' ')

    def __str__(self):
        return self.workedYears
