username = input('Username: ')
while True:
  try:
    password = int(input('Password: '))
    break
  except Exception as e:
    print('lol fail rip')

if username == 'jb007' and password == 123:
  print('Welcome.')
elif username == '':
  print('Enter details')
else:
  print('Incorrect')