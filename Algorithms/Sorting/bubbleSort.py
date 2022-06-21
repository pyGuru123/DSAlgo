# Bubble Sort

import random

def bubbleSort(arr):
	for i in range(len(arr) - 1):
		for j in range(len(arr) - 1 - i):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

lst = [random.randint(1,100) for i in range(10)]
random.shuffle(lst)
print("Before Sorting")
print(lst)
print("After Sorting")
bubbleSort(lst)
print(lst)