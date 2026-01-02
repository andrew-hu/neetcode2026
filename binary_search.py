# https://www.w3schools.com/python/python_dsa_binarysearch.asp

def binarySearch(arr, targetVal):
	left = 0
	right = len(arr) - 1

	while left <= right:
		middle = (left + right) // 2
		if targetVal == arr[middle]:
			return middle
		if targetVal > arr[middle]:
			left = middle + 1
		else: # if targetVal is less than arr[middle]
			right = middle - 1
	return -1


mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 11

result = binarySearch(mylist, x)

if result != -1:
  print("Found at index", result)
else:
  print("Not found")

