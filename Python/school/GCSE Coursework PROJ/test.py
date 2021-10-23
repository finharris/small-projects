import csv
import os

nameList = []
passList = []
highscoreList = []

datafilename = "authusers.csv"
datafiledir = "csv"
data_file = os.path.join(datafiledir, datafilename)

with open(data_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        nameList.append(row.get('name'))
        passList.append(row.get('password'))
        highscoreList.append(row.get('hscore'))


username = input('What is your username?')
if username in usernames: 
	print('Welcome.')

	password = input('What is your password?')
	userIndex = usernames.index(username)
	if password == passwords[userIndex]:
		print('Correct')

		theirHS = highscores[userIndex]
