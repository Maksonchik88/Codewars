from math import ceil, floor
def add(*args):
    l = list(args)
    if len(l) == 0:
        return 0
    else:
        numb = 0
        i = 1
        for num in l:
            if abs(num) >= i:
                numb += ceil(num / i)
            else:
                numb += floor(num / i)
            i += 1
        return numb


print(add(-1, -2, -3, -4))
