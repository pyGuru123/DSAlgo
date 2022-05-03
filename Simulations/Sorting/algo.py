def insertionSort(arr, length):
	for i in range(1, length):
		while i > 0 and arr[i-1] > arr[i]:
			temp = arr[i-1]
			arr[i-1] = arr[i]
			arr[i] = temp

			i -= 1
		print(arr)


array = [5, 2, 4, 6, 1, 9, 3, 7, 8, 0]
length = len(array)
print(array)
insertionSort(array, length)