def oddandevenwhile(num): # defines the function with one peraimter needed
	i = 0 # creates a variable i to count how many itterations have happened
	while i <= num: # this will keep running till i is greater than the users number
		if i % 2 == 0: # checks if i is even
			print("{} is an even number.".format(i)) # tells user i is even
		else: # else or if i is odd
			print("{} is an odd number.".format(i)) # tells user i is odd
		i += 1 # adds one to i otherwise the same thing will keep happening

oddandevenwhile(21) # 21 can be whatever number you want. the call of this function needs to have the peramiter or an error will be shown

def oddandevenfor(num): # defines the function with one peraimter needed
	for i in range(0, num+1): # this does the same as the while loop but without needing to declare the variable before and add one to after, also, it needs to be num+1 because the second peramiter is not inclusive
		if i % 2 == 0: # checks if i is even
			print("{} is an even number.".format(i)) # tells user i is even
		else: # else or checks if i is odd
			print("{} is an even number.".format(i)) # tells user i is odd

oddandevenfor(21) # 21 can be whatever number you want. the call of this function needs to have the peramiter or an error will be shown