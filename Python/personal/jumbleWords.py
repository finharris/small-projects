import random
import re

sentence = input("Please type a sentence to be jumbled: ").lower()
sentence = re.sub(r'[^\w\s]', '', sentence)

sentenceArr = sentence.split(" ")
random.shuffle(sentenceArr)

if type(sentenceArr[0]) == str:
    sentenceArr[0] = sentenceArr[0].capitalize()
else:
    pass

outputSen = ""
for word in sentenceArr:
    if word != sentenceArr[len(sentenceArr)-1]:
        outputSen += f"{word} "
    else:
        outputSen += f"{word}."

print(outputSen)
