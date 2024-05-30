# Nth Highest Salary leetcode 117

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    result= [] 
    for i in range(len(employee)): 
        salary= employee['salary'][i]
        if salary not in result:
            result.append(salary)   
    result.sort(reverse= True)  
    if N > len(result) or N <= 0: 
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]}) 
    return pd.DataFrame({f'getNthHighestSalary({N})': [result[N-1]]}) 


#using set
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    resultSet = set()
    for i in range(len(employee)):
        salary= employee['salary'][i]
        resultSet.add(salary)
    result=[]
    for element in resultSet:
        result.append(element)
    result.sort(reverse= True)
    if N > len(result) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})':[None]})
    return pd.DataFrame({f'getNthHighestSalary({N})': [result[N-1]]})
    
    
#Shorter method
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee[['salary']].drop_duplicates()
    if N > len(df) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    return df.sort_values('salary', ascending= False).head(N).tail(1)[['salary']].rename(columns = {'salary' : f'getNthHighestSalary({N})'})