def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]  # Swap using tuple unpacking
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)  # Partitioning index
        quickSort(array, low, pi - 1)    # Sort left partition
        quickSort(array, pi + 1, high)  # Sort right partition

data = [1, 7, 4, 1, 10, 9, -2]
size = len(data)
print("Unsorted Array")
print(data)

quickSort(data, 0, size - 1)

print("Sorted Array in Ascending Order:")
print(data)
