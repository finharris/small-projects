import csv
import sys
import os

cost = []
items = []

filename = "products.csv"
filedir = ""
csv_file = os.path.join(filedir, filename)

names = []
description = []
price = []

with open(csv_file, 'r') as f:
	reader = csv.DictReader(f)
	for row in reader:
		names.append(row.get('name'))
		description.append(row.get('description'))
		price.append(row.get('price'))

# Print all items
print("All items in stock:\n")
for i in range(len(names)):
	print(names[i], ",", description[i], ", £", price[i])

requestic = int(input("How many items do you want?"))
ic = 0
shopping = True
while shopping:
	if requestic != ic:
		request = str(input("Requested item name: "))
		for i in range(len(names)):
			if names[i].lower() == request.lower():
				cost.append(price[i])
				items.append(names[i])
				ic += 1
	else:
		everything = str(input("Is that everything? Y/N"))
		if everything.lower() == "y":
			shopping = False
		elif everything.lower() == "n":
			requestic += 1
		else:
			print("Invalid input. Exiting.")
			sys.exit()

totalcost = 0
for i in range(len(cost)):
	totalcost += float(cost[i])

print("Please pay your total cost of £" + str(totalcost), "for:", items)

transactionprog = True
while transactionprog:
	paid = float(input("How much are you paying? £"))
	if paid > totalcost:
		print("Dispensing change of: £" + str(round(paid - totalcost, 2)))
		print("Thanks for shopping with us! Have a great day.")
		transactionprog = False
	else:
		print("You need to add more money. All money returned. Please input more money.")
