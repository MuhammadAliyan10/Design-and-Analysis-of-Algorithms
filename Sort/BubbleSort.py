def BubbleSort(array):
    for i in range(len(array) - 1, -1, -1):  
        swapped = False 
        for j in range(i): 
            if array[j] > array[j + 1]:  
                array[j], array[j + 1] = array[j + 1], array[j]  
                swapped = True  
        if not swapped:  
            break
    return array 

array = [64, 34, 25, 12, 22, 11, 90]
sortedArray = BubbleSort(array)
print(sortedArray)
