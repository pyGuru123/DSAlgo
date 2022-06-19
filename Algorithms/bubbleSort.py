# Bubble Sort

import random

def bubbleSort(lst):

	for i in range(len(lst) - 1):		for j in range(len(lst) - 1 - i):

			if lst[j] > lst[j+1]:

				lst[j], lst[j+1] = lst[j+1], lst[j]

				

list_ = [random.randint(1,100) for i in range(10)]

random.shuffle(list_)

print("Before Sorting")

print(list_)

print("After Sorting")

bubbleSort(list_)

print(list_)
