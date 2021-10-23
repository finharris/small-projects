a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

def binarySearch(data, target):
	import math

	data.sort()

	if not data:
		return False

	if target > data[len(data)-1] or target < data[0]:
		print('Out of range')
		return False

	pivot = round((len(data)-1) / 2)

	print(f'data: {data}\ntarget: {target}\npivot: {data[pivot]}\n')

	if target == data[pivot]:
		return data[pivot]
	elif target < data[pivot]:
		# remove anything after and including pivot
		return binarySearch(data[0:pivot], target)
	elif target > data[pivot]:
		# remove anything before and including the pivot
		return binarySearch(data[pivot+1:len(data)], target)

print(binarySearch(a, 14))