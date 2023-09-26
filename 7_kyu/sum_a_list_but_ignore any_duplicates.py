def sum_no_duplicates(l):
    my_dict = {}
    for el in l:
        if my_dict.get(el, None):
            my_dict[el] += 1
        else:
            my_dict[el] = 1
    count = 0
    for key, val in my_dict.items():
        if val == 1:
            count += key
    return count


