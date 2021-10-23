# a = 2
# b = 3
# c = a + b
#
# print("The output is " + "\"" + str(c) + "\"")
# a = int(input("Num 1: "))
# b = int(input("Num 2: "))
# c = a + b
#
# print("The output is " + "\"" + str(c) + "\"")
# a = str(input("Word 1: "))
# b = str(input("Word 2: "))
# c = a + b
#
# print("The output is " + "\"" + str(c) + "\"")
# a = float(input("Float 1: "))
# b = float(input("Float 2: "))
# c = a + b
#
# print("The output is " + "\"" + str(c) + "\"")
# a = str(input("Word: "))
# b = int(input("Num: "))
# c = a * b
#
# print("The output is " + "\"" + str(c) + "\"")

coruser = "Fin"
corpass = "Password"

while True:
    username = input("Username: ")

    if username == coruser and str.islower(coruser) != True:
        userbool = True
        break
    else:
        print("Incorrect, try again.")
        continue

while True:
    password = input("Password: ")

    if password == corpass and str.islower(password) != True:
        passbool = True
        break
    else:
        print("Incorrect, try again.")
        continue

if userbool == True and passbool == True:
    print("You are in.")
else:
    print("ACCESS DENIED!")