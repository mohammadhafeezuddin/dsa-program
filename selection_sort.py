def selection_sort(n, arr):
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print("pass:", i + 1, arr)


n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

print("Original array:", arr)
selection_sort(n, arr)
print("Sorted array:", arr)
