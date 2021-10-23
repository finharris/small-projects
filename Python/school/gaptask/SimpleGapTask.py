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

filename = "names.csv"
filedir = ""
csv_file = os.path.join(filedir, filename)

with open(csv_file) as file:
	reader = csv.DictReader(file)
	name = row[0]
	names.append(name)

names = []

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
		# add student
		addname = str(input("Enter the name of the student you want to add: "))
		names.append(addname)
	elif menuinput == "2":
		# search student
		searchforname = str(input("Enter the name of the student you want to search for: "))
		for name in names:
			if name.lower() == searchforname.lower():
				print("Found {}.".format(name))
	elif menuinput == "3":
		# sort students
		print("Sorting...")
		names.sort()
		print("Sorted:\n{}".format(names))
	elif menuinput == "4":
		# remove student
		while True:
			delname = str(input("Enter the name of the student you want to remove: "))
			count = 0
			for name in names:
				if name.lower() == delname.lower():
					print("Name found. Removing...")
					names.remove(name)
					break
				else:
					count += 1

				if count == len(names):
					print("Name not found, try again")
					continue
	elif menuinput == "5":
		# log out
	else:
		print("Not a valid option. Please pick one of the numbers.")
		continue