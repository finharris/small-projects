import time
import csv
import random

lines = open("words.csv").read().splitlines()
word = random.choice(lines)

wordarray = []
corarray = []
wrong_guesses = []
wordlen = len(word)
tries = 10
correct = False
templetter = ""

for c in word:
  corarray.append("-")

for letter in word:
  wordarray.append(letter)


def addletter(character):
  for i in range(len(wordarray)):
    if wordarray[i] == character:
      corarray.pop(i)
      corarray.insert(i, character)


print("Welcome to hangman.\nThe word you are guessing is {} letters long.".format(wordlen))
print("You have {} guesses in total.".format(tries))

guesses = 1
while guesses <= tries:
  print("\nGuess number {} out of {}.".format(guesses, tries))
  print(f"Word so far: {' '.join(corarray)}")
  print(f'Current wrong guesses: {", ".join(wrong_guesses)}')
  time.sleep(.2)
  while True:
    guess = str(input("Guess a letter: "))
    if len(guess) != 1:
      print("Not one letter.")
    else:
      break
  for letter in word:
    if letter.lower() == guess.lower():
      print("One letter correct.")
      templetter = letter
      addletter(letter)
      if corarray == wordarray:
        correct = True
        break
      else:
        pass
    else:
      pass
  if templetter.lower() != guess.lower():
    print("Wrong!")
    wrong_guesses.append(guess.lower())
    guesses += 1

  if correct:
    break

if correct:
  print("You won! The word was \"{}\".".format(word))
  time.sleep(2)
else:
  print("You ran out of guesses :(. Better luck next time! The word was {}.".format(word))
  time.sleep(2)
