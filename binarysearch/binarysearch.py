def binarysearchfirstlargerthangivennum(array, num):
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

def binarysearchlastequalgivennum(array, num):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) >> 1
        if num < array[mid]:
            right = mid - 1
        elif num >= array[mid]:
            left = mid + 1
    if right >= 0 and array[right] == num:
        return right
    return 0

# print binarysearchlastequalgivennum([1,3,3,4], 3)

def BinarySearchDomain(array, num):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) >> 1
        if num < array[mid]:
            right = mid - 1
        elif num > array[mid]:
            left = mid + 1
        else:
            left_domian = left + binarysearchfirstlargerthangivennum(array[left:mid+1], num)
            right_domian = mid + binarysearchlastequalgivennum(array[mid:right+1], num) + 1
            return left_domian, right_domian

    return -1


print BinarySearchDomain([1, 3,3,4,4],4)