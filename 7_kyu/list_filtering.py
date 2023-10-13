def filter_list(test_list: list) -> list:
    ret_list = []
    for el in test_list:
        if type(el) is int:
            ret_list.append(el)
    return ret_list

print(filter_list([1, 2, 'a', 'b']))
print(filter_list([1, 'a', 'b', 0, 15]))
