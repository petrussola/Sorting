test = [1, 3, 2]
test2 = [4, 7, 5]


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    merged_arr = arrA + arrB
    return merged_arr


print(merge(test, test2))
