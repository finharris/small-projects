test = 'This is a cool translator.'

key = {
  'a': '4',
  'e': '3',
  'g': '6',
  'l': 1,
  'o': '0',
  's': '5',
  't': '7',
  'z': '2'
}

def translate(input):
  output = []
  for letter in input:
      if letter in key:
         output.append(str(key[letter]))
      else:
         output.append(str(letter))
  return ''.join(output)


print(translate(test))