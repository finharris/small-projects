class Averages:
    def average():
        import sys
        import statistics
        import math

        numbers = []

        def calculateMean(nums):
            return sum(nums) / len(nums)

        def calculateMedian(nums):
            nums.sort()
            print(nums)
            return nums[math.floor(len(nums)/2)]

        def calculateMode(nums):
            return max(nums, key=nums.count)

        def writeNumbers(nums):
            nums.append()
            stringNums = [str(i) + '\n' for i in nums]
            with open('nums.txt', 'w') as f:
                f.writelines(stringNums)

        def askWriteNumbers(nums, message):
            if input('Write numbers to nums.txt? (y/n)') == 'y':
                        numbers.append('')
                        writeNumbers(nums)
            else:
                return

        print('Please enter numbers. (type \'calc\' to calculate the result and type \'quit\' to exit the program)')

        addingNumbers = True
        while addingNumbers:
            try:
                newNum = input('- ')
            except Exception as e:
                print(f'There was an error [{e}]')

            if newNum == 'calc':
                averageChoice = input(
                    'Calculate \'mean\', \'median\' or \'mode\' (or 1, 2 or 3)? ')

                answer = ''
                if averageChoice == 'mean' or averageChoice == '1':
                    answer = calculateMean(numbers)
                    print(answer)
                    askWriteNumbers(numbers, f'mean = {answer}')
                elif averageChoice == 'median' or averageChoice == '2':
                    answer = calculateMedian(numbers)
                    print(answer)
                    askWriteNumbers(numbers, f'median = {answer}')
                elif averageChoice == 'mode' or averageChoice == '3':
                    answer = calculateMode(numbers)
                    print(answer)
                    askWriteNumbers(numbers, f'mode = {answer}')

                break
            elif newNum == 'quit':
                break
            elif newNum.replace(' ', '') == '':
                continue
            else:
                try:
                    numbers.append(int(newNum))
                except Exception as e:
                    print(f'There was an error [{e}]')
