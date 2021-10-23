sentence = input("Enter sentence: ").split(" ")
whatWord = input("What word do you want to replace?: ")

for i in range(len(sentence)):
    if sentence[i] == whatWord:
        sentence[i] = "changed"
    else:
        pass

outputSen = ""
for word in sentence:
    if word != sentence[len(sentence)-1]:
        outputSen += f"{word} "
    else:
        outputSen += f"{word}."

print(f"\n\n{outputSen}")
