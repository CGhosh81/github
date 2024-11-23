def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid  # Return the index if the element is found
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Return -1 if the element is not found

arr = [10, 20, 30, 40, 50]
key = 30

result = binary_search(arr, key)

if result != -1:
    print(f"Element {key} found at index {result}")
else:
    print(f"Element {key} not found")
