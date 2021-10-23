import time
import sys

while True:
  curflr = int(input('What floor are you on?'))
  if curflr < 0:
    print('Invalid floor.')
  else:
    break

while True:
  while True:
    while True:
      try:
        reqflr = int(input("What floor do you want to go to (-1 to exit)? "))
        if reqflr < -1:
          raise ValueError
        break
      except ValueError:
        print("Not a valid number... Try again. \n")
    if reqflr == -1:
      sys.exit(0)
    
    if reqflr == curflr:
      print("Already on that floor.")
      continue
    else:
      break

  while curflr != reqflr:
    if curflr > reqflr:
      # go down
      curflr -= 1
      print("You are now on floor {}.".format(curflr))
      time.sleep(.3)
    elif curflr < reqflr:
      # go up
      curflr += 1
      print("You are now on floor {}.".format(curflr))
      time.sleep(.3)

  if curflr == reqflr:
    print("Opening doors.")