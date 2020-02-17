test = [4, 2, 2, 8, 3, 3, 1]


def count_sort(arr):
    max_value = max(arr)
    len_count_list = max_value + 1
    count_list = [0] * len_count_list
    for i in range(0, len(arr)):
        count_list[arr[i]] += 1
    return count_list


print(count_sort(test))
