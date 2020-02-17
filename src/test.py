test = [4, 2, 2, 8, 3, 3, 1]


def count_sort(arr):
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


print(count_sort(test))
