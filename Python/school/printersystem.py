queueitems = []
paperamt = 0

while True:
	while True:
		try:
			paperamt = paperamt + int(input("How much paper would you like to add (currently {} paper in printer (max. 20))?".format(paperamt)))
			if paperamt <= 20:
				break
			else:
				print("Too large a number\n")
				continue
		except ValueError:
			print("Not a number. Try again.\n")

	while True:
		queuecount = len(queueitems)
		if queuecount == 20:
			print("Must print items before adding more.")
			break
		else:
			additem = str(input("What item would you like to add to the queue? "))
			queueitems.append(additem)
			while True:
				again = str(input("Would you like to add another (y/n)? "))
				if again.lower() == "y" or again.lower() == "n":
					break
				else:
					print("Invalid answer. Try again.\n")
			if again.lower() == "y":
				continue
			elif again.lower() == "n":
				break
	queuecount = len(queueitems)
	if paperamt < queuecount:
		print("Not enough paper. Please add more and try again.")
		queuecount = 0
		queueitems = []
	while queuecount > 0:
		print("Printing {}".format(queueitems[0]))
		paperamt -= 1
		queueitems.remove(queueitems[0])
		queuecount = len(queueitems)

	if queuecount == 0:
		printagn = str(input("Nothing left to print. Would you like to print again (y/n)? "))
		if printagn.lower() == "y":
			continue
		elif printagn.lower() == "n":
			print("Ok.")
			break
		else:
			print("Not a valid input.")
