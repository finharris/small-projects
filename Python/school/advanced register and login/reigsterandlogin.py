import csv
import os

def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

menu = """
1. Remove User
2. Log Out
"""

usernames = []
passwords = []

filename = "data.csv"
filedir = ""
csv_file = os.path.join(filedir, filename)

with open(csv_file) as file:
	reader = csv.reader(file)
	for row in reader:
		username = row
		password = row
		usernames.append(username[0])
		passwords.append(password[1])

def register():
	while True:
		inpusername = str(input("Enter the username you want to use username (0-10 chars): "))
		if len(inpusername) >= 1 and len(inpusername) <=10:
			print("Username correct length.\n")
			count = 0
			for user in usernames:
				if user == inpusername:
					print("Username already in use.")
					continue
				else:
					count += 1
			if count == len(usernames):
				break
		else:
			print("Username incorrect lenght.\n")
			continue
	while True:
		inppassword = str(input("Enter the password you want to use password (at least one upper and one lowercase character and at least one number): "))
		inppassword2 = str(input("Please reenter the password to confirm: "))
		if inppassword == inppassword2:
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

	print("Username and password valid.")
	usernames.append(inpusername)
	passwords.append(inppassword)
	print("Please login with your new credentials.")

loginorregister = str(input("Would you like to 1) login or 2) register? "))
if loginorregister == "1":
	pass
else:
	register()

while True:
	index = 0
	loggedin = False
	while True:
		enterusername = str(input("Username: "))
		count = 0
		for i in range(len(usernames)):
			if usernames[i] == enterusername:
				print("Found user.\n")
				index = i
				break
			else:
				count += 1
		if count == len(usernames):
			print("User not found. Try again.\n")
		else:
			break
	while True:
		enterpassword = str(input("Password: "))
		if enterpassword == passwords[index]:
			print("Correct.\n")
			loggedin = True
			break
		else:
			print("Incorrect password. Please login again.\n")
			break
	if loggedin:
		break

print("Welcome {}. ".format(usernames[index]), end="")
while True:
	print("\nChoose one of the following:")
	print(menu)

	menuinput = str(input(" - "))

	if menuinput == "1":
		# remove user
		usertoremove = str(input("\nEnter user to remove: "))
		count = 0
		for i in range(len(usernames)):
			if usernames[i] == usertoremove:
				if i == index:
					print("Cannot remove yourself.")
					break
				else:
					removepassword = passwords[i]
					usernames.remove(usernames[i])
					passwords.remove(removepassword)
			else:
				count += 1
		if count == len(usernames):
			print("User not found.")
		print(usernames, passwords)
	elif menuinput == "2":
		# log out
		# clear csv
		f = open(csv_file, "w+")
		f.close()

		# add usernames and passwords to csv
		a = []
		for i in range(len(usernames)):
			temp = [usernames[i], passwords[i]]
			a.append(temp)
		print(a)
		with open(csv_file, "w", newline="") as f:
			writer = csv.writer(f)
			writer.writerows(a)
		break
	else:
		print("Not a valid option. Try again.\n")