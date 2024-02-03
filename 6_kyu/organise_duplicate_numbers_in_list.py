def group(arr: list[int]) -> list[list]:
    new_dict = dict((i, arr.count(i)) for i in arr)
    res_list = []
    for k, v in new_dict.items():
        res_list.append([k] * v)
    return res_list



print(group([3, 2, 6, 2, 1, 3]), [[3, 3], [2, 2], [6], [1]])
print(group([3, 2, 6, 2]), [[3], [2, 2], [6]])
print(group([]), [])
print(([1, 100, 4, 2, 4]), [[1], [100], [4, 4], [2]])
print(group([-1, 1, -1]), [[-1, -1], [1]])