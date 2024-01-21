def track_sum(arr):
    a = arr
    b = sorted(set(a), reverse=True)
    c = [(x-y) for (x, y) in zip(b, b[1:])]
    d = sorted(set(c), key=c.index)
    return [list(map(sum,[a,b,c,d])), d]