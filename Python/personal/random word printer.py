import os
import random

filename = "words.txt"
filepath = "C:\\Users\\finch\\Documents"

file = os.path.join(filepath, filename)

count = 0
wordcount = 1

array = []

while count < wordcount:
	count += 1
	with open(file) as f:
	    content = f.readlines()

	content = [x.strip() for x in content] 

	word = random.choice(content)

	array.append(word)


sentence = "{}.".format(" ".join(array).capitalize())
print(sentence)