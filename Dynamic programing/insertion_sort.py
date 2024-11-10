def insertionSort(arr): 

    n = len(arr)  # Get the length of the array 
    if n <= 1: 
        return  # If the array has 0 or 1 element, it is already sorted, so return 
    for i in range(1, n):  # Iterate over the array starting from the second element 

        key = arr[i]  # Store the current element as the key to be inserted in the right position 
        j = i-1
        print(arr) 
        print("----------------------")
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead 
            arr[j+1] = arr[j]  # Shift elements to the right 
            j -= 1
            print(arr) 
            print("----------------------",j)
        arr[j+1] = key 
        print(arr)
        print("----------------------",i)
arr = [12, 11, 13, 5, 6] 

insertionSort(arr) 

print(arr) 