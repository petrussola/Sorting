# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # cur_index = i
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        temp_low = arr[smallest_index]
        arr[smallest_index] = arr[i]
        arr[i] = temp_low
        # cur_index += 1
        smallest_index = i
    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    has_swapped = True
    while has_swapped:
        has_swapped = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                has_swapped = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    max_value = max(arr)
    count_list = [0] * (max_value + 1)
    cum_count = 0
    output = [0] * len(arr)
    for i in range(0, len(arr)):
        count_list[arr[i]] += 1
    for i in range(0, len(count_list)):
        cum_count += count_list[i]
        count_list[i] = cum_count
    for item in arr:
        if item in output:
            output.count(item)
            where = output.index(item)
            output[where - 1] = item
        else:
            output[count_list[item] - 1] = item
    return output
