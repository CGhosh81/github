def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i  # Return the index if the element is found
    return -1  # Return -1 if the element is not found

arr = [10, 20, 30, 40, 50]
key = 30

result = linear_search(arr, key)

if result != -1:
    print(f"Element {key} found at index {result}")
else:
    print(f"Element {key} not found")
