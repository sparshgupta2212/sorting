def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [45, 66, 11, 15, 5, 78, 98, 88, 35, 28]
print(bubbleSort(arr))
