# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        temp_low = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp_low
        cur_index += 1
        smallest_index = cur_index
    return arr


def sel_sort(list):
    cur_index = 0
    # smallest_index = cur_index
    for i in range(cur_index, len(list) - 1):
        for j in range(cur_index + 1, len(list) - 1):
            if list[j] < list[i]:
                temp = list[j]
                del list[j]
                list.insert(0, temp)
    return list

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
