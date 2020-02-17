test = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


# def test_list(list, index):
#     temp = list[index]
#     del list[index]
#     list.insert(0, temp)
#     return list


# print(test_list(test, 2))

def sel_sort(list):
    cur_index = 0
    smallest_index = cur_index
    for i in range(cur_index, len(list) - 1):
        for j in range(cur_index + 1, len(list)):
            if list[j] < list[smallest_index]:
                smallest_index = j
        temp_low = list[smallest_index]
        list[smallest_index] = list[cur_index]
        list[cur_index] = temp_low
        # list.insert(cur_index, temp)
        cur_index += 1
        smallest_index = cur_index
    return list


print(sel_sort(test))
