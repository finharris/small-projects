import hashlib
import csv
import os


casesensitive = False


def hasher(passw):
    hashed = hashlib.md5(passw)
    return hashed.hexdigest()


def singup():
    username = input("Enter User Name: ").lower()
    password = hasher(input("Password: ").encode("utf-8"))

    fields = ['username', 'password']

    filename = 'data.csv'

    # Open file in append mode
    with open(filename, 'a', newline='\n') as csvUser:
        dicti = {'username': username, 'password': password}

        writer = csv.DictWriter(csvUser, fieldnames=fields)

        # if it's an empty file, write the header
        if os.stat(filename).st_size == 0:
            writer.writeheader()

        writer.writerow(dicti)

    csvUser.close()


def login():
    usernames = []
    passwords = []

    csv_file = 'data.csv'

    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            usernames.append(row.get('usernames'))
            passwords.append(row.get('passwords'))

    loggedin = False
    while not loggedin:
        username = input("What is your username? ")
        if casesensitive:
            password = input("What is your password? ").encode("utf-8")
        else:
            password = input("What is your password? ").lower().encode("utf-8")
        hashpassword = hasher(password)

        for i in range(len(usernames)):
            if username.lower() == usernames[i].lower():
                if hashpassword == passwords[i]:
                    print("You have been logged in, {}.".format(username.capitalize()))
                    loggedin = True
                else:
                    print("Invalid login details. Try again.")


def main():
    if casesensitive:
        print("Password case sensitivity is ON.\n")
    else:
        print("Password case sensiticity is OFF.\n")

    mainbool = True
    while mainbool:
        choice = str(input("Welcome to the hashed password signup and login.\nTo sign up, type \"1\"\nTo login, type \"2\"\n\t: "))
        if choice == "1":
            singup()
            mainbool = False
        elif choice == "2":
            login()
            mainbool = False
        else:
            print("Invalid input, try again.")
            continue


if __name__ == "__main__":
    main()
