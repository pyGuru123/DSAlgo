# Insertion Sort

import random

def insertionSort(arr):
	for i in range(len(arr)):
		key = arr[i]
		j = i - 1
		while (j>=0 and key < arr[j]):
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key
				
lst = [random.randint(1,100) for i in range(10)]
random.shuffle(lst)
print("Before Sorting")
print(lst)
print("After Sorting")
insertionSort(lst)
print(lst)