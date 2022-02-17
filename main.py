import pandas as pd

data = pd.read_csv('test2.csv')
print(data)
print(data.Subject)             #can use data.[column name] to print that whole column. very helpful...

#using article https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/