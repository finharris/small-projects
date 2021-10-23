# Two numbers print biggest

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

if a > b:
	print(a)
else:
	print(b)

# If same print 0 else add

c = int(input("Enter number 1: "))
d = int(input("Enter number 2: "))

if c == d:
	print(c-d)
else:
	print(c+d)

# One larger, one factor

e = int(input("Enter number 1 (larger): "))
f = int(input("Enter number 2 (factor): "))

if e%f == 0:
	while e >= 0:
		print(e)
		e -= f

# Print 3 numbers in order

g = int(input("Enter number 1: "))
h = int(input("Enter number 2: "))
i = int(input("Enter number 3: "))

array = []
array.append(g)
array.append(h)
array.append(i)
array.sort()

for i in range(len(array)):
	if i < len(array)-1:
		print("{}, ".format(array[i]), end="")
	else:
		print("{}".format(array[i]), end="")