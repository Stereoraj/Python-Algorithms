'''
	Python script to implement the sorting algorithm
'''

def selectionSort(arr):
	for i in range(0, len(arr)):
		min = i

		for j in range(i+1, len(arr)):
			if(arr[j] < arr[min]):
				min = j

		arr[i], arr[min] = arr[min], arr[i]

	return arr

def mergeSort(arr):
	if(len(arr) == 1):
		return arr
	
	mid = len(arr) / 2
	left = mergeSort(arr[0:mid])
	right = mergeSort(arr[mid:])
	merged = Merge(left, right)
	
	return merged

def Merge(left, right):
	merged = []

	while(len(left) != 0 and len(right) != 0):
		item1 = left[0]
		item2 = right[0]
		
		if(item1 <= item2):
			merged.insert(len(merged), left.pop(0))				
		else:
			merged.insert(len(merged), right.pop(0))
		
	# insert the remaining elements to merged list
	if(len(left) != 0):
		for i in range(len(left)):
			merged.insert(len(merged), left[i])
	if(len(right) != 0):
		for i in range(len(right)):
			merged.insert(len(merged), right[i])
	
	return merged

def quickSort(unsortedList, left, right): 
	if(left >= right):	
		return

	pivot = partition(unsortedList, left, right)

	quickSort(unsortedList, left, pivot - 1)
	quickSort(unsortedList, pivot + 1, right)

	return unsortedList

def partition(unsortedList, left, right):
	# set the pivot
	x = unsortedList[left]

	j = left

	for i in range(left + 1, right):
		if(unsortedList[i] <= x):
			j = j + 1
			unsortedList[j], unsortedList[i] = unsortedList[i], unsortedList[j]

	unsortedList[left], unsortedList[j] = unsortedList[j], unsortedList[left]

	return j

if __name__ == "__main__":
	# initialize the sample test case
	arr = [5, 9, 20, 14, 3]
	# print("Using selection sort -> " + str(selectionSort(arr)))
	print("Merge Sort : ", mergeSort(arr))
	print("Quick Sort : ", quickSort(arr, 0, len(arr)));
