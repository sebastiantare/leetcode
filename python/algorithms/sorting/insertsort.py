def insertionsort(arr):
    u = 1  # Unsorted
    while u < len(arr):
        hold = arr[u]
        i = u - 1
        while i >= 0 and hold < arr[i]:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = hold
        u += 1
    return arr

print(insertionsort([4, 2]))
print(insertionsort([2, 2, 4, 75, 2, 74, 54]))
print(insertionsort([1, 2, 3]))
print(insertionsort([1, 2, 5, 3]))
