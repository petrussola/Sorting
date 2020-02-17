test = [4, 2, 2, 8, 3, 3, 1]


def count_sort(arr):
    max_value = max(arr)
    len_count_list = max_value + 1
    count_list = [0] * len_count_list
    cum_count = 0
    for i in range(0, len(arr)):
        count_list[arr[i]] += 1
    for i in range(0, len(count_list)):
        cum_count += count_list[i]
        count_list[i] = cum_count

    return count_list


print(count_sort(test))
