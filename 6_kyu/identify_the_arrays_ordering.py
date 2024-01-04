def order_type(arr):
    len_list = []
    for el in arr:
        if type(el) == int:
            len_list.append(len(str(el)))
        else:
            len_list.append(len(el))

    if len(len_list) in (0, 1) or len(set(len_list)) == 1:
        return 'Constant'
    elif sorted(len_list) == len_list:
        return 'Increasing'
    elif sorted(len_list, reverse=True) == len_list:
        return 'Decreasing'
    else:
        return 'Unsorted'



print(order_type([1, "b", ["p"], 2]), "Constant")
print(order_type([123, 1234, 12345, 123456]), "Increasing")
print(order_type(["a", "abc", "abcde", "ab"]), "Unsorted")
print(order_type([[1, 2, 3, 4], [5, 6, 7], [8, 9]]), "Decreasing")
print(order_type([1, 2, 3, 4, 56]), "Increasing")
print(order_type([["ab", "cdef", "g"], ["hi", "jk", "lmnopq"], ["rst", "uv", "wx"], ["yz"]]), "Decreasing")
print(order_type([[1, 23, 456, 78910], ["abcdef", "ghijklmno", "pqrstuvwxy"],
                               [[1, 23, 456, 78910, ["abcdef", "ghijklmno", "pqrstuvwxy"]], 1234]]), "Decreasing")
print(order_type([]), "Constant")
print(order_type(["pippi", "pippi", "batuffulo", "pippi"]), "Unsorted")
print(order_type(["pippi"]), "Constant")