import random

class guessTheNumber:
  def __init__(self, numRange=(0,100), maxTries=5):
    super().__init__()
    if len(numRange) != 2: raise TypeError
    self.number = random.randint(numRange[0], numRange[1])
    self.tries = 1
    self.maxTries = maxTries
  
  def setup(self):
    newRange = (int(input('First number in range: ')), int(input('Second number in range: ')))
    self.number = random.randint(newRange[0], newRange[1])

    self.maxTries = int(input('Max tries: '))
  
  def play(self):
    num = self.number

    guess = int(input('Guess: '))
    if guess == num:
      print(f'Correct, the answer was {num}')
      return True

    if self.tries == self.maxTries:
      print(f'Took too many tries ({self.tries}). The answer was {num}.')
      return False

    if guess > num: print('Guess is too high.')
    elif guess < num: print('Guess is too low.')

    self.tries += 1
    self.play()


a = guessTheNumber()
a.setup()
a.play()
del a
