'''
	Python script to implement the selection sort
'''

def selectionSort(arr):
	for i in range(0, len(arr)):
		min = i

		for j in range(i+1, len(arr)):
			if(arr[j] < arr[min]):
				min = j

		arr[i], arr[min] = arr[min], arr[i]

	return arr

if __name__ == "__main__":
	arr = [5, 9, 20, 14, 3]
	print(selectionSort(arr))
