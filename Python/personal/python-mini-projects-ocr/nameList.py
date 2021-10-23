'''
Basic lists
Make a program that lets a user input a series of names into a list. The program should then ask the user whether they want to print out the list in the original order, or in reverse.
Extensions:
1. Enable the user to choose what number item in the list they want to print out
2. Enable the user to only print out a ‘slice’ of the list (eg item three to item nine only)
3. Enable the user to remove any items of the list that they want to
4. Enable the user to save their list to a file for later, and also enable them to load it back up again too
5. ‘Clean’ the list by making all the items lowercase
'''


class NameList:
    def makeList(self):
        listData = []

        def printData():
            def printOneByOne(lst):
                for i in range(0, len(lst)):
                    if i == len(lst)-1:
                        print(lst[i])
                    else:
                        print(f'{lst[i]}, ', end='')

            chosen = False
            while not chosen:
                choice = input(
                    'Would you like to print \'normal\', \'reverse\' or \'single\'? ')
                if choice == 'normal':
                    printOneByOne(listData)
                    chosen = True
                elif choice == 'reverse':
                    reversedListData = listData
                    reversedListData.reverse()
                    printOneByOne(reversedListData)
                    chosen = True
                elif choice == 'single':
                    while True:
                        try:
                            printIndex = int(
                                input('Which place do you want to print? ')) - 1
                            print(listData[printIndex])
                            break
                        except Exception as e:
                            if e == TypeError:
                                print('Please input a number.\n')
                            elif e == IndexError:
                                print('That place does not exist in the list.\n')
                            else:
                                print(f'There was an error. [{e}]\n')
                    chosen = True
                else:
                    print('Not an option, try again.\n')

            return

        print('Please enter data for the list spaced with commas (no spaces after comma) or one by one then enter \'print\' to get output options.\n')
        while True:
            userInput = input(' :')
            if userInput == 'print':
                printData()
                break
            else:
                listData.extend(userInput.split(','))

        return
