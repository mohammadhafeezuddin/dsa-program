def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while i < high and arr[i] <= pivot:
            i = i + 1
        while arr[j] > pivot:
            j = j - 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j


n = int(input("Enter no. of elements: "))
arr = []
for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

print("Original array:", arr)
quick_sort(arr, 0, n - 1)
print("Sorted array:", arr)
