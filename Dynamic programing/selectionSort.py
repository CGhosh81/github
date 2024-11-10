def selectionSort(arr, size):
    n=size
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    return arr

arr = [-2, 45, 0, 11, -9,88,-97,-202,747] 
size = len(arr) 
selectionSort(arr,size) 
print('The array after sorting in Ascending Order by selection sort is:') 
print(arr) 