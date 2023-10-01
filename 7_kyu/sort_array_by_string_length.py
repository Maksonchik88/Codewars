def sort_by_length(arr):
    d = {}
    for elem in arr:
        d[elem] = len(elem)
    sorted_d = sorted(d.items(), key=lambda item: item[1])
    return list(map(lambda x: x[0], sorted_d))
