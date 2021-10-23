english = ['hello', 'goodbye']
spanish = ['hola', 'adios']

userInput = input('Enter word to be translated: ')

if userInput in english:
  print(f'{userInput} in spanish is: {spanish[english.index(userInput)]}')
else:
  print('Not found, check spelling.')