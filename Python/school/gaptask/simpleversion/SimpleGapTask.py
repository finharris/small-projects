import csv
import os
import random

def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

menu = """
1. Add Students
2. Search Student
3. Sort Students
4. Remove Student
5. View students
6. Shuffle Students
7. Log out

\\\\Type cancel at any time to come back here\\\\
"""

names = []

filename = "names.csv"
filedir = ""
csv_file = os.path.join(filedir, filename)

with open(csv_file) as file:
	reader = csv.reader(file)
	for row in reader:
		name = row
		names.append(name[0])

while True:
	while True:
		inpusername = str(input("Enter your username: "))
		if len(inpusername) >= 1 and len(inpusername) <=10:
			print("Username correct length.\n")
			break
		else:
			print("Username incorrect lenght.\n")
			continue
	while True:
		inppassword = str(input("Enter your password: "))
		if inppassword.lower() != inppassword and inppassword.upper() != inppassword:
			print("Username correct capitalisation.")
			if hasNumbers(inppassword):
				print("Username has numbers.")
				break
			else:
				print("Username does not have numbers.\n")
				continue
		else:
			print("Username incorrect capitalisation.\n")
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
		print("\nAdded {}.".format(addname))
	elif menuinput == "2":
		# search student
		searchforname = str(input("Enter the name of the student you want to search for: "))
		count = 0
		for name in names:
			if name.lower() == searchforname.lower():
				print("\"{}\" exists in the system.".format(name))
			else:
				count += 1

			if count == len(names):
				print("Could not find \"{}\" in the system.".format(searchforname))
	elif menuinput == "3":
		# sort students
		print("Sorting...")
		names.sort()
		print("Sorted: ")
		for i in range(len(names)):
			if i != len(names)-1:
				print("{}, ".format(names[i]), end='')
			else:
				print("{}.".format(names[i]))
	elif menuinput == "4":
		# remove student
		while True:
			delname = str(input("Enter the name of the student you want to remove: "))
			count = 0
			for name in names:
				if name.lower() == delname.lower():
					print("Name found. ", end="")
					while True:
						confirmation = str(input("Are you sure you want to delete {}? y/n".format(name)))
						if confirmation.lower() == "y":
							print("Removing...")
							names.remove(name)
							break
						elif confirmation.lower() == "n":
							print("Ok, won't delete.")
							break
						else:
							print("Not a valid answer. Try again.\n")
							continue
					break
				else:
					count += 1

				if count == len(names):
					print("Name not found, try again")
					continue
			break
	elif menuinput == "5":
		# view students
		print("\nHere are all students currently in the system:")
		for name in names:
			print(" - {}".format(name))
	elif menuinput == "6":
		# shuffle students
		print("Shuffling students.")
		random.shuffle(names)
		print("Shuffled: ")
		for i in range(len(names)):
			if i != len(names)-1:
				print("{}, ".format(names[i]), end='')
			else:
				print("{}.".format(names[i]))
	elif menuinput == "7":
		# log out
		print("\nLogging out...")
		# clear csv file
		f = open(csv_file, "w+")
		f.close()

		# write array (names) to file
		with open(csv_file, "w", newline='') as f:
			wtr = csv.writer(f)
			for x in names:
				wtr.writerow([x])
		break
	else:
		print("Not a valid option. Please pick one of the numbers shown.")
		continue