# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
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
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
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


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
