def selectionSort(array):
    n = len(array)
    for i in range(n):

        minimum = i
        for j in range(i + 1, n):
            if (array[j] < array[minimum]):
                minimum = j
        temp = array[i]
        array[i] = array[minimum]
        array[minimum] = temp
    return array
array = [99, 55, 29, 1, 56, 35, 45, 75, 89, 52]
print(selectionSort(array))
