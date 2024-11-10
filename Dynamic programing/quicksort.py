def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        print(array)
        if array[j] <= pivot:
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            print(i)
            print(array)
    temp = array[i + 1]
    array[i + 1] = array[high]
    array[high] = temp
    print(i)
    print(array)
    return i + 1
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        print(pi)
        quickSort(array, low, pi - 1)
        print(pi)
        quickSort(array, pi + 1, high)
data = [1, 7, 4, 1, 10, 9, -2]
size = len(data)
print("Unsorted Array")
print(data)
quickSort(data, 0, size - 1)
print("Sorted Array in Ascending Order:")
print(data)
