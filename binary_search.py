def binary_search(n, arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


n = int(input("Size of array: "))
arr = []
print("Enter array elements:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter key: "))
result = binary_search(n, arr, key)

if result == -1:
    print("Unsuccessful")
else:
    print(f"Key is found at {result}")
