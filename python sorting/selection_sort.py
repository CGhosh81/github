
def SelectionSort(arr):
    n = len(arr)
    for i in range(n):
     for j in range(i+1,n):
        if arr[i] > arr[j]:
             temp=arr[i]
             arr[i]=arr[j]
             arr[j]=temp
    return arr
arr = [-2,45,0,11,-9,88,-97,-202,747]

print("Unsorted list is:")
print(arr)

print("Sorted list is:")
print(SelectionSort(arr))
