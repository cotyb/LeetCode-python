def binarysearch(array, num):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) >> 1
        if num <= array[mid]:
            right = mid - 1
        elif num > array[mid]:
            left = mid + 1
    if left < len(array):
        return left
    return -1



print binarysearch([3,3,4],1)