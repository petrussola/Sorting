test = [3, 2, 1]


def find(arr, item):
    try:
        find = arr.index(item)
        return find
    except:
        return 'not found'


print(find(test, 4))
