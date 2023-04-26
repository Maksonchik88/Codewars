def flatten_and_sort(array):
    new_list = []
    for lst in array:
        for num in lst:
            new_list.append(num)
    new_list = sorted(new_list)
    return new_list

print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]))
print(flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]]))
