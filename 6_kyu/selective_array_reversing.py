def sel_reverse(arr: list, l: int) -> list:
    '''Creating a reverse function.'''
    if l == 0:
        return arr
    else:
        return list(reversed(arr)) if len(arr) <= l else split_into_sublists(arr, l)


def split_into_sublists(arr: list, l: int) -> list:
    new_arr = [arr[i:i + l] for i in range(0, len(arr), l)]
    rev_arr = []
    for el in new_arr:
        rev_arr.append(list(reversed(el)))
    return sum(rev_arr, [])

print(sel_reverse([2, 4, 6, 8, 10, 12, 14, 16], 3)),
print(sel_reverse([2, 4, 6, 8, 10, 12, 14, 16], 2)),
print(sel_reverse([1, 2, 3, 4, 5, 6], 2)),
print(sel_reverse([1, 2, 3, 4, 5, 6], 0)),
print(sel_reverse([1, 2, 3, 4, 5, 6], 10))