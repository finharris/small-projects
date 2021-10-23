"""
def oddandeven(num):
	for i in range(num + 1):
		if i%2 == 0:
			print("{} is an even number.".format(i))
		else:
			print("{} is an odd number.".format(i))

oddandeven(64)
"""

"""
for i in range(1,101):
    output = ""
    
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    if output == '':
        output += str(i)
    print(output)
"""

"""
def timestables():
	for num in range(0, 11):
		for i in range(0, 11):
			print("the value of {} x {} = {}".format(num, i, num*i))

timestables()
"""