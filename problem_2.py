#Second Highest Salary leetcode 176

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salaries=set()
    for i in range(len(employee)):
        salary=employee['salary'][i]
        salaries.add(salary)
    result=[]
    for salary in salaries:
        result.append(salary)
    result.sort(reverse= True)
    if 2> len(result):
        return pd.DataFrame([None], columns = ['SecondHighestSalary'])
    return pd.DataFrame([result[1]], columns = ['SecondHighestSalary'])

#other Method

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(['salary'])
    if len(employee) < 2 :
        return pd.DataFrame([None], columns = ['SecondHighestSalary'])
    employee = employee.sort_values('salary', ascending= False)
    employee.drop('id', axis = 1, inplace= True)
    employee.rename({'salary' : 'SecondHighestSalary'}, axis =1, inplace = True)
    return employee.head(2).tail(1)
