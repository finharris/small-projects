attempts = 0

details = {
  'username': 'username',
  'password': 'password'
}

responses = [
  'Incorrect.',
  'Nope.',
  'Try again.',
  'Cmon, man.',
  'Not quite.',
  'Bro, for real?',
  'You made the password, not me...',
  'YO, Whats your problem?',
  'Get it right already.',
  'This is getting out of hand.',
  'I give up.'
]

while True:
  inpu = input('enter username')
  if inpu == details['username']:
    break
  else:
    pass


loggedIn = False
while not loggedIn:
  inpp = input('Enter password: ')
  if inpp == details['password']:
    print('Correct.')
    loggedIn = True
  else:
    if attempts < len(responses)-1:
      print(responses[attempts])
    else:
      print(responses[len(responses)-1])
      break


  attempts += 1