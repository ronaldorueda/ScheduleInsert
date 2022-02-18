import pandas as pd

data = pd.read_csv('test2.csv')
print(data)
print(data.Subject)             #can use data.[column name] to print that whole column. very helpful...

clientList = list() #will gran subject to let us know who the client is
dateList = list()
beginningTimeList = list()
endTimeList = list()
descriptionList = list() #will grab description to grab link to enter time entries / should also have small description to write to time entries



#using article https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/