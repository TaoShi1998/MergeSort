def mergesort(unsorted):
    if len(unsorted) <= 1:
        return unsorted
    size = len(unsorted)/2
    left_unsorted = mergesort(unsorted[:size])
    right_unsorted = mergesort(unsorted[size:])
    left = 0
    right = 0
    result = []
    while left < len(left_unsorted) or right < len(right_unsorted):
        if left < len(left_unsorted) and (right == len(right_unsorted) or left_unsorted[left]<=right_unsorted[right]):
            result.append(left_unsorted[left])
            left += 1
        else:
            result.append(right_unsorted[right])
            right += 1
    return result


print("排序前：12, -3, 5, 27, 19, 2, 10, 15, 90, 1")
print("排序后："+mergesort([12, -3, 5, 27, 19, 2, 10, 15, 90, 1]))










