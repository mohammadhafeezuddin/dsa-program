def insertion_sort(n, arr):
    for i in range(1, n):
        ele = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > ele:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = ele
        print("pass:", i, arr)


n = int(input("Enter no. of elements: "))
arr = []
for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

print("Original array:", arr)
insertion_sort(n, arr)
print("Sorted array:", arr)
