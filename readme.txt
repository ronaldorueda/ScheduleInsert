This repository is to automate time entries based off of Outlook calendar csv exports. The problem that had led me to begin this project is the excessive amount of time it takes to perform time entries. 
In the dev team, we do a good job of planning our day in our Outlook calendars to let team members and management know what we are working on the hour, and I want to take that export and automate time entries.

This script will go through the csv export and grab time and dates off and enter them into specified Smartsheets or Base99 tickets.
Currently the script is able to loop through the csv file based off the headers and assigning them to respective lists. After doing minimal research, I was not able to find a better solution to loop through rows via Pandas.
For now, as mentioned priorly, I use multiple for loops to go through each header that I need to get data from.
For the time being, I believe it is not ideal to create a class with the respected fields, but subject to change as I continue to chug along as I do not like this current approach.

More exact documentation as this grows will be added.

The documentation I have used to get started was based off the following article:
https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/

URL for Pandas:
https://pandas.pydata.org/docs/index.html

I am always open to feedback and criticism (seriously please criticize me and make me do better as I want to improve)

Thanks!
