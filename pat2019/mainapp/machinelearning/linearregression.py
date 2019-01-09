import pandas as pd
from sklearn.linear_model import LinearRegression


def prepare_data(salary):
    salary['salaryBrutto'] = pd.to_numeric(salary['salaryBrutto'], errors='coerce')
    salary_train = salary[salary['salaryBrutto'].notnull()]
    salary_test = salary[salary['salaryBrutto'].isnull()]
    return salary_train, salary_test


def train_model(salary_train):
    X = salary_train[['workedYears']]
    y = salary_train['salaryBrutto']
    model = LinearRegression()
    model.fit(X,y)
    return model


def predict_salary(model, salary_test):
    predictions = model.predict(salary_test[['workedYears']])
    salary_test.loc[:, 'salaryBruttoPredicted'] = pd.Series(predictions, index=salary_test.index)
    return salary_test


def result(salary_train, salary_test):
    salary_out = salary_train.append(salary_test)
    salary_out = salary_out[['id', 'workedYears', 'salaryBrutto', 'salaryBruttoPredicted']]
    return salary_out


def calculate_predicted_salary(data):
    salary = pd.DataFrame(list(data.values()))
    salary_train, salary_test = prepare_data(salary)
    model = train_model(salary_train)
    salary_test = predict_salary(model, salary_test)
    return result(salary_train, salary_test)



