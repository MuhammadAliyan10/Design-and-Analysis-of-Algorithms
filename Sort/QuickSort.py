def QuickSort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return QuickSort(left) + middle + QuickSort(right)

array = [3, 6, 8, 10, 1, 2, 1]
sortedArray = QuickSort(array)
print(sortedArray)
