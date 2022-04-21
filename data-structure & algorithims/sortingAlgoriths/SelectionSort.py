def selectionSort(arr):
    size = len(arr)
    for step in range(size):
        min_index = step
        for i in range(step+1,size):
            if arr[i] < arr[min_index]:
                min_index = i
        (arr[step],arr[min_index]) = (arr[min_index],arr[step])
arr = [12,2222,-200,34,23,333,37,-11,-2,0]
selectionSort(arr)
print(arr)