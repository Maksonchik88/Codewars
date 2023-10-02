def quick_sort(lst: list) -> list:
    if len(lst) <= 1:
        return lst

    elem = lst[0]
    less_lst = list(filter(lambda el: el < elem, lst))
    equals_lst = [el for el in lst if el == elem]
    more_lst = list(filter(lambda el: el > elem, lst))

    return quick_sort(less_lst) + equals_lst + quick_sort(more_lst)




print(quick_sort([5]))
print(quick_sort([5, 3, 33, 58, 4, 8, 9, 0, 22, 1, 1, 3, 9]))