from ..models import SalaryPredicted


def update_salary_predicted(salary_predicted):
    print(salary_predicted)
    salary_list = []
    SalaryPredicted.objects.all().delete()

    for index, row in salary_predicted.iterrows():
        salary_list.append(SalaryPredicted(workedYears=row["workedYears"], salaryBrutto=row["salaryBrutto"], salaryBruttoPredicted=row["salaryBruttoPredicted"]))

    SalaryPredicted.objects.bulk_create(salary_list)
