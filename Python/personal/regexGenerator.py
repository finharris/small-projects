import pyperclip # type: ignore

def menu():
  menu = [
    ("Unique Items (e.g. This, That, The Other)", uniqueItems),
    ("Semi-similar items (e.g. 1 Star, 2 Star, 3 Star)", semiSimilar)
  ]
  
  # List out all the menu options
  while True:
    for i, item in enumerate(menu):
      print(f'{i+1}: {item[0]}')
    selection = input("\nChoose menu item (or 'q' to quit): ")
    if selection.lower() == 'q':
      print("Exiting.")
      return
    if selection.isdigit() and 1 <= int(selection) <= len(menu):
      return menu[int(selection)-1][1]()
    else:
      print("Invalid selection. Please try again.")

def getItemsFromUser(additionalText=""):
  items = []
  print("\n" + additionalText)
  howMany = input("How many items?")
  for i in range(int(howMany)):
    item = input("Item: ")
    items.append(item)
  return items

def convertItemsToRegex(items):
  regex = "("
  first = True
  for item in items:
    if first:
      regex += f"{item}"
      first = False
    else:
      regex += f"|{item}"
  regex += ")"
  return regex

def uniqueItems():
  items = getItemsFromUser()
  return convertItemsToRegex(items)
  

def semiSimilar():
  # Get the template and values from the user
  similarPart = input("Enter the part similar to all inputs. Add '**' for where the rest should be filled in:")
  # similarPart = "** Star COMPLETE"
  parts = similarPart.split("**")
  
  # values = input("Enter the different values, separated by commas: ")
  values_list = getItemsFromUser(additionalText="Input all the values to go into where the ** was.")

  results = []
  for value in values_list:
      # Join the parts with the value inserted at the split(s)
      result = value.join(parts)
      results.append(result)
  
  return convertItemsToRegex(results)
  

if __name__ == "__main__":
  output = menu()
  if output != None:
    print(output)
    pyperclip.copy(output)
    print("\n\nOUTPUT COPIED TO CLIPBOARD")
  # semiSimilar()