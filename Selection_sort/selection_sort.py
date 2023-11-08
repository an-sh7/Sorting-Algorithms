def main(array):
	length = len(array)
	
	for i in range(length):
		min_index = i
		for j in range (i+1,length):
			if array[j] < array[min_index]:
				min_index = j

		array[i], array[min_index] = array[min_index], array[i]




array = [34,52,41,31,643,24]
main(array)
print("Sorted Array is:", array)