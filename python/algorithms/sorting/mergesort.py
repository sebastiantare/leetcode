def mergesort(arr):
    if len(arr) < 2:
        return arr

    m = len(arr)//2
    left = arr[:m]
    right = arr[m:]

    mergesort(left)
    mergesort(right)

    # To merge ordered the left and right array we have to
    # iterate over both arrays and fill the new array with the values
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # If there are any leftover values in the left half, fill them in
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Otherwise fill the leftover values from the right half
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


print(mergesort([4, 2]))
print(mergesort([2, 2, 4, 75, 2, 74, 54]))
print(mergesort([1, 2, 3]))
print(mergesort([1, 2, 5, 3]))
