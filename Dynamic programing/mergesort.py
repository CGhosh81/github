def merge(arr, l, r):
    mid = l + (r - l) // 2
    n1 = mid - l + 1  # Length of left half
    n2 = r - mid      # Length of right half
    
    # Create temporary arrays
    L = arr[l:mid + 1]
    R = arr[mid + 1:r+1]
    
    i = 0    # Initial index of left subarray
    j = 0    # Initial index of right subarray
    k = l    # Initial index of merged subarray
    
    # Merge the two halves back into arr
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    # Copy remaining elements of L, if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    # Copy remaining elements of R, if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, l, m)       # Sort first half
        mergeSort(arr, m + 1, r)   # Sort second half
        merge(arr, l, r)           # Merge the sorted halves

# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
print(arr)

mergeSort(arr, 0, n -1)
print("\nSorted array is")
print(arr)
