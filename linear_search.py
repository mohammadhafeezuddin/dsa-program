def linear_search(n, arr, key):
    for i in range(len(arr)):
        if key == arr[i]:
            return i
    return -1


n = int(input("Size of array: "))
arr = []
print("Enter array elements:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter key: "))
result = linear_search(n, arr, key)

if result == -1:
    print("Unsuccessful")
else:
    print(f"Key is found at {result}")
