'''
Letter list 
Write a program that lets a user choose a letter. The program will then find all the words beginning with that letter in a list and print them out. It should also say how many words it found.
Extensions: 
1. Let the user load up a list of words from a file and have the program process them all
'''


class LetterSearch:
    def search(self):
        while True:
            char = input('Please enter the starting letter to search for: ')
            if len(char) != 1:
                print('Invalid length.')
                pass
            else:
                break

        def printOneByOne(lst):
            for i in range(0, len(lst)):
                if i == len(lst)-1:
                    print(lst[i])
                else:
                    print(f'{lst[i]}, ', end='')

        wordList = ['one', 'two', 'three', 'obo']

        if input('Would you like to load from a file? y/n') == 'y':
            fileName = input(
                'Please enter the name of the file including ".txt": ')
            with open(fileName, 'r') as f:
                for line in f:
                    wordList.append(line.strip('\n'))
            pass
        else:
            pass

        foundCount = 0
        foundList = []

        for word in wordList:
            if list(word)[0] == char:
                foundCount += 1
                foundList.append(word)

        print(f'Found {foundCount} matches.')
        printOneByOne(foundList)
        return
