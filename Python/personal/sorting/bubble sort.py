a = [3, 4, 7, 5, 1, 8, 0, 2, 6, 9]


def bubblesort(data):
	issorted = False

	while not issorted:
		swaps = 0
		for i in range(0, len(data) - 1):
			if data[i + 1] < data[i]:
				data[i], data[i + 1] = data[i + 1], data[i]
				swaps += 1

		if not swaps:
			issorted = True

	return data


# print(bubblesort(a))



nums = [3, 4, 7, 5, 1, 8, 0, 2, 6, 9]

# let swaps
# loop
# swaps = false
# compare i and i + 1, if i + 1 > i then swap
# if not then swaps = true
# sorted when not swaps


def sortthisbubble(numbers):
	while True:
		for i in range(0, len(numbers)-1):
			swaps = False
			if numbers[i+1] < numbers[i]:
				numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
				swaps = True

			if not swaps:
				return numbers

print(sortthisbubble(nums))





















