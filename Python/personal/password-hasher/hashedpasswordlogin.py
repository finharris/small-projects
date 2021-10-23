import hashlib
import csv

usernames = []
passwords = []

csv_file = 'data.csv'

with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        usernames.append(row.get('usernames'))
        passwords.append(row.get('passwords'))


def hasher(passw):
    hashed = hashlib.md5(passw)
    return hashed.hexdigest()


loggedin = False
while not loggedin:
    username = input("What is your username? ")
    password = input("What is your password? ").encode("utf-8")
    hashpassword = hasher(password)

    for i in range(len(usernames)):
        if username.lower() == usernames[i].lower():
            if hashpassword == passwords[i]:
                print("You have been logged in.")
                loggedin = True
