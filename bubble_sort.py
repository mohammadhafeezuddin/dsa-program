def bubble_sort(n, arr):
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print("pass:", i + 1, arr)


n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

print("Original array:", arr)
bubble_sort(n, arr)
print("Sorted array:", arr)
