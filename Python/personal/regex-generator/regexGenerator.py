import pyperclip # type: ignore
import os

def menu():
  menu = [
    ("Unique Items (e.g. This, That, The Other)", uniqueItems),
    ("Semi-similar items (e.g. 1 Star, 2 Star, 3 Star)", semiSimilar),
    ("CSV List (e.g. a .csv file containing 'Item 1, Item2, Item 3')", csvList)
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
      os.system("clear")
      print("--Invalid selection. Please try again--\n")


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


def csvList():
  # csv contents: item 1, item 2, item 3, item 4
  filename = input("Enter the name of the CSV file (e.g. items.csv): ")
  filepath = os.path.join(os.path.dirname(__file__), filename)
  try:
    with open(filepath, "r", encoding="utf-8") as f:
      lines = f.readlines()
      if len(lines) != 1:
        print("Error: CSV file must contain only one line with items separated by commas.")
        return
      content = lines[0].strip()
      # Split by comma and strip whitespace from each item
      items = [item.strip() for item in content.split(",")]
      return convertItemsToRegex(items)
  except FileNotFoundError:
    print("Error: File not found. Please make sure the file is in the same directory as this script.")
    return


if __name__ == "__main__":
  output = menu()
  if output != None:
    print(f"\n\n --OUTPUT-- \n\n{output}")
    pyperclip.copy(output)
    print("\n\nOUTPUT COPIED TO CLIPBOARD")
  # semiSimilar()