import csv
import os

def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

menu = """
1. Add Students
2. Search Student
3. Sort Students
4. Remove Student
5. Log out
"""

filename = "studentinfo.csv"
filedir = ""
csv_file = os.path.join(filedir, filename)

names = []
ages = []
emails = []

with open(csv_file) as file:
	reader = csv.DictReader(file)
	for row in reader:
		names.append(row.get('name'))
		ages.append(row.get('age'))
		emails.append(row.get('email'))

while True:
	while True:
		inpusername = str(input("Enter your username: "))
		if len(inpusername) >= 1 and len(inpusername) <=10:
			print("Username correct length.")
			break
		else:
			print("Username incorrect lenght.")
			continue
	while True:
		inppassword = str(input("Enter your password: "))
		if inppassword.lower() != inppassword and inppassword.upper() != inppassword:
			print("Username correct capitalisation.")
			if hasNumbers(inppassword):
				print("Username has numbers.")
				break
			else:
				print("Username does not have numbers.")
				continue
		else:
			print("Username incorrect capitalisation.")
			continue

	if inpusername == "MrToms" and inppassword == "Password1":
		print("Correct username and password.")
		break
	else:
		print("incorrect username and password.")
		continue

print("\nWelcome {}.".format(inpusername))
while True:
	print("\n{}".format(menu))
	menuinput = str(input(" - "))

	if menuinput == "1":
		while True:
			# add student
			newname = str(input("Please enter the students name: "))
			newage = str(input("Please enter the stidents age: "))
			newemail = str(input("Please enter the students email: "))
			fields=[newname,newage,newemail]
			with open(csv_file, 'a') as f:
			    writer = csv.writer(f)
			    writer.writerow(fields)
			addanother = str(input("Would you like to add another student? (y/n) "))
			if addanother.lower() == "y":
				continue
			elif addanother.lower() == "n":
				names = []
				ages = []
				emails = []
				with open(csv_file) as file:
					reader = csv.DictReader(file)
					for row in reader:
						names.append(row.get('name'))
						ages.append(row.get('age'))
						emails.append(row.get('email'))
				break
			else:
				print("Not a valid input...")
	elif menuinput == "2":
		# search student
		searchby = str(input("Would you like to search by 1. Name, 2. Age, or 3. Email? "))
		if searchby == "1":
			while True:
				searchforname = str(input("What is the name of the student you want to search for? "))
				print("\n")
				for i in range(len(names)):
					if names[i].lower() == searchforname.lower():
						print("Information for {}:\nName - {}\nAge - {}\nEmail - {}\n".format(names[i], names[i], ages[i], emails[i]))
				searchanother = str(input("Would you like to search for another student by name? (y/n) "))
				if searchanother.lower() == "y":
					continue
				elif searchanother.lower() == "n":
					break
				else:
					print("Not a valid input...")
					break
		elif searchby == "2":
			while True:
				searchforage = str(input("What is the age of the student you want to search for? "))
				print("\n")
				for i in range(len(ages)):
					if ages[i].lower() == searchforage.lower():
						print("Information for {}:\nName - {}\nAge - {}\nEmail - {}\n".format(names[i], names[i], ages[i], emails[i]))
				searchanother = str(input("Would you like to search for another student by age? (y/n) "))
				if searchanother.lower() == "y":
					continue
				elif searchanother.lower() == "n":
					break
				else:
					print("Not a valid input...")
					break
		elif searchby == "3":
			while True:
				searchforemail = str(input("What is the email of the student you want to search for? "))
				print("\n")
				for i in range(len(emails)):
					if ages[i].lower() == searchforemail.lower():
						print("Information for {}:\nName - {}\nAge - {}\nEmail - {}\n".format(names[i], names[i], ages[i], emails[i]))
				searchanother = str(input("Would you like to search for another student by email? (y/n) "))
				if searchanother.lower() == "y":
					continue
				elif searchanother.lower() == "n":
					break
				else:
					print("Not a valid input...")
					break
	elif menuinput == "3":
		# sort students
		print("Sorted names:\n")
		sortednames = names
		sortednames.sort()
		for i in range(len(names)):
			print(names[i])
		print("\nDone!")
	elif menuinput == "4":
		# remove student
		break
	elif menuinput == "5":
		# log out
		print("Logging out.")
		break
	else:
		print("Not a valid option. Please pick one of the numbers.")
		continue