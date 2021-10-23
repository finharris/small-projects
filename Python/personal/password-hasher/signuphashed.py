import hashlib
import csv
import os


def hasher(passw):
    hashed = hashlib.md5(passw)
    return hashed.hexdigest()


userName = input("Enter User Name: ")
passWord = hasher(input("Password: ").encode("utf-8")).lower()

fields = ['username', 'password']

filename = 'data.csv'

# Open file in append mode
with open(filename, 'a', newline='\n') as csvUser:
    dict = {'username': userName,'password': passWord}

    writer = csv.DictWriter(csvUser, fieldnames=fields)

    # if it's an empty file, write the header
    if os.stat(filename).st_size == 0:
        writer.writeheader()

    writer.writerow(dict)

csvUser.close()