 # denery to binary and hex
def hasNumbers(string):
	count = 0
	for char in string:
		if char.isdigit():
			count += 1
		else:
			pass
	if count == len(string):
		return True
	else:
		return False

while True:
	convertfrom = input("What number do you want to convert? ")
	if hasNumbers(convertfrom):
		convertfrom = int(convertfrom)
		break
	else:
		print("Not a number, try again.\n")

binconv = bin(convertfrom)
hexconv = hex(convertfrom)

choice = str(input("Would you like to convert to 1) Binary, 2) Hexidecimal or 3) Both? "))
if choice == "1":
	print("{} in binary is \"{}\".".format(convertfrom, binconv[2:]))
elif choice == "2":
	print("{} in hex is \"{}\".".format(convertfrom, hexconv[2:]))
elif choice == "3":
	print("{} in binary is \"{}\" and in hex is \"{}\".".format(convertfrom, binconv[2:], hexconv[2:]))


 # Bubble sort
def bubbleSort(arr):
	count = 0
	while count < len(arr) -1:
		count = 0
		for i in range(len(arr) - 1):
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
			else:
				count += 1


 # read and write to csv
import os
import csv

names = []
addresses = []
phones = []

filename = "info.csv"
filedir = ""
csv_file = os.path.join(filedir, filename)

with open(csv_file) as file:
	reader = csv.reader(file)
	for row in reader:
		name = row
		address = row
		phone = row
		names.append(name[0])
		addresses.append(address[1])
		phones.append(phone[2])

f = open(csv_file, "w+")
f.close()

a = []
for i in range(len(names)):
	temp = [names[i], addresses[i], phones[i]]
	a.append(temp)
with open(csv_file, "w", newline="") as f:
	writer = csv.writer(f)
	writer.writerows(a)