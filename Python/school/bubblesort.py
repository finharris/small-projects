def bubbleSort(arr):
  count = 0
  while count < len(arr) -1:
    count = 0
    for i in range(len(arr) - 1):
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
      else:
        count += 1

import random

elements = 2000



from datetime import datetime

for i in range(7000, 7001, 1000):
  array = []
  for i in range(0,i + 1):
    array.append(random.randint(0,i + 1))

  now = datetime.now()
  # print("Before: {}".format(array))
  bubbleSort(array)
  now2 = datetime.now()
  
  difference = now2-now
  print(f'Time taken for {i} elements: {difference}')

if sorted(array) == array:
  print("Sorted =", True)
else:
  print("Sorted =", False)

# current_time = now.strftime("%H:%M:%S")
# current_time2 = now2.strftime("%H:%M:%S")
# print(now)
# print(now2)

