def mergeSort(arr):
    if len(arr) == 1:
        return
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)
    merge(arr, left, right)
    return arr

def merge(arr, left, right):
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[i+j] = left[i]
            i += 1
        else:
            arr[i+j] = right[j]
            j += 1

    while i < len(left):
        arr[i+j] = left[i]
        i += 1

    while j < len(right):
        arr[i+j] = right[j]
        j += 1

    return arr

sample = [2, 5, 1, 3, 7, 4, 2, 3, 9, 8, 6, 3]
mergeSort(sample)
print(sample)