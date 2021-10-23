curflr = 0

while True:
	while True:
		try:
			reqflr = int(input("What floor do you want to go to? "))
			break
		except ValueError:
			print("Not a number... Try again. \n")
	if reqflr == curflr:
		print("Already on that floor.")
		continue
	else:
		break

while curflr != reqflr:
	if curflr > reqflr:
		# go down
		curflr -= 1
		print("You are now on floor {}.".format(curflr))
	elif curflr < reqflr:
		# go up
		curflr += 1
		print("You are now on floor {}.".format(curflr))

if curflr == reqflr:
	print("Opening doors.")