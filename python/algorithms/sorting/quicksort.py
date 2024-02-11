def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = [arr[0]]
        less = []
        greater = []

        for i in arr[1:]:
            if i == pivot[0]:
                pivot.append(i)
            if i < pivot[0]:
                less.append(i)
            if i > pivot[0]:
                greater.append(i)

        return quicksort(less) + pivot + quicksort(greater)

print(quicksort([4, 2]))
print(quicksort([2, 2, 4, 75, 2, 74, 54]))
print(quicksort([1,2,3]))
