import random
import os

WORDS = open("words.csv").read().splitlines()

OBFUSCATED_DELIMITER = '*'
ALLOWED_GUESSES = 7

HANGMAN_STATES = [
  '''
  
  ''',
  '''
  ___
  ''',
  '''
  |
  |
  ___
  ''',
  '''
  ___
  |
  |
  ___
  ''',
  '''
  ___
  | |
  |
  ___
  ''',
  '''
  ___
  | |
  | o
  ___
  ''',
  '''
  ___
  | |
  | o
  | |
  ___
  ''',
  '''
  ___
  | |
  | o
  | |
  |/ \\
  ___
  ''',
]

def clear():
  os.system('cls')


def getWord(words):
  choice = input('Random word or custom word? ("r" or "c") ')
  
  if choice.lower() == 'r':
    word = random.choice(words)
  elif choice.lower() == 'c':
    word = input('Please enter the word: ')
    
  return word


def splitWord(word):
  new_word = []
  for c in word:
    new_word.append(c)
  return new_word


def joinList(lst):
  word = ''
  for c in lst:
    word += c
  return word


def getObfuscatedList(word, guessed_chars):
  if not guessed_chars:
    word_list = list(OBFUSCATED_DELIMITER * len(word))
    return word_list
  
  word_list = []
  
  for c in word:
    if c in guessed_chars:
      word_list.append(c.lower())
    else:
      word_list.append(OBFUSCATED_DELIMITER)
      
  return word_list
  

def printIncorrect(lst):
  output = ''
  for c in lst:
    output += f'{c}, '
  return output[0:-2]


def main():
  clear()

  word = getWord(WORDS)
  split_word = splitWord(word)
  
  guesses = []
  incorrectGuesses = set()
  
  clear()

  guesses_count = 0
  while guesses_count < ALLOWED_GUESSES:  
    obfuscated_list = getObfuscatedList(word,guesses)
    
    if OBFUSCATED_DELIMITER not in obfuscated_list:
      print(f'\nYou win! The word was "{word}".')
      break
    
    print('\n\n')
    print(joinList(obfuscated_list),end='\n\n')
    
    guess = input('Guess: ')
    if len(guess) != 1:
      print('Not a valid guess.')
      continue
      
    clear()


    if guess in guesses or guess in incorrectGuesses:
      print('Already guessed.')
    elif guess in split_word:
      print('Correct!')
      guesses.append(guess.lower())
    else:
      incorrectGuesses.add(guess.lower())
      print('Incorrect!')
      guesses_count += 1
    
    print(f'{ALLOWED_GUESSES - guesses_count} guesses left.')
    print(HANGMAN_STATES[guesses_count])

    print(f'Already guessed wrong: {printIncorrect(incorrectGuesses)}')
  
  if guesses_count >= ALLOWED_GUESSES:
    print(f'The man was hung. Better luck next time. The word was "{word}".')
      

if __name__ == '__main__':
  main()