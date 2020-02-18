test = [1, 3, 2]
test2 = [4, 7, 5]
test3 = [7, 3, 1, 6, 9, 4, 5, 2, 8]
test4 = [12, 21, 34, 21, 45, 67, 54, 38, 9, 5, 2, 17, 28]


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    # check first items in arrays and place the smallest one as position of new array
    for k in range(elements):
        if len(arrA) == 0:
            merged_arr[k] = arrB[0]
            del arrB[0]
        elif len(arrB) == 0:
            merged_arr[k] = arrA[0]
            del arrA[0]
        else:
            if arrA[0] < arrB[0]:
                merged_arr[k] = arrA[0]
                del arrA[0]
            else:
                merged_arr[k] = arrB[0]
                del arrB[0]
    # if one array is empty and the other one has one item left, add this item to the array without further check

    return merged_arr


# print(merge(test, test2))

def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    lhs = arr[:middle]
    rhs = arr[middle:]
    left = merge_sort(lhs)
    right = merge_sort(rhs)
    return merge(left, right)


print(merge_sort(test4))
