def bbSort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if (arr[i] > arr[j]):
                aux = arr[j]
                arr[j] = arr[i]
                arr[i] = aux
    return arr


arr1 = [1]
arr2 = [1, 2]
arr3 = [2, 1]
arr4 = [1, 0, 2, 3, 3]

print(bbSort(arr1))
print(bbSort(arr2))
print(bbSort(arr3))
print(bbSort(arr4))
