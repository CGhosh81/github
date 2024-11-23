
def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
     for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
             temp=arr[j]
             arr[j]=arr[j+1]
             arr[j+1]=temp
    return arr
arr = [39,12,18,85,72,10,2,18]
print("Unsorted list is:")
print(arr)

print("Sorted list is:")
print(BubbleSort(arr))
