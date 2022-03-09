import pandas as pd                 #pandas is a tool to go through csv files
from datetime import date           #needed to get today's date since it will always be ran at the end of day

data = pd.read_csv('test2.csv')
#print(data)
#print(data.Subject)                #can use data.[column name] to print that whole column. very helpful...

clientList = list()                 #will grab subject to let us know who the client is
todaysDate = date.today()           #today's date
beginningTimeList = list()          #beginning time of each item in calendar
endTimeList = list()                #end time of each item in calendar
descriptionList = list()            #will grab description to grab link to enter time entries / should also have small description to write to time entries
siteList = list()                   #grab the site these entries need to be made to

#loop through Subject from csv and append to clientList
for item in data.Subject:
    clientList.append(item)

#loop to get start times and add to beginList
for item in data.StartTime:
    beginningTimeList.append(item)

#loop to get end times and add to endList
for item in data.EndTime:
    endTimeList.append(item)

#loop to get descriptions and sites to their lists
for item in data.Description:
    descriptionList.append(item[0:item.index(';')])
    siteList.append(item[(item.index(';') + 1) : (len(item) - 1)])

