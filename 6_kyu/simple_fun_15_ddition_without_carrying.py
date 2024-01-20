def addition_without_carrying(a, b):
    a, b = list(reversed(str(a))), list(reversed(str(b)))
    if len(a) > len(b):
        b.extend([0, ] * (len(a) - len(b)))
    elif len(a) < len(b):
        a.extend([0, ] * (len(b) - len(a)))

    a, b = list(reversed(a)), list(reversed(b))
    new_list = []
    for i in range(len(a)):
        if int(a[i]) > int(b[i]):
            if (int(a[i]) + int(b[i])) <= 9:
                new_list.append((int(a[i]) + int(b[i])))
            else:
                temp = (int(a[i]) + int(b[i])) - 10
                new_list.append(temp)
        elif int(a[i]) <= int(b[i]):
            if (int(a[i]) + int(b[i])) <= 9:
                new_list.append((int(a[i]) + int(b[i])))
            else:
                temp = (int(b[i]) + int(a[i])) - 10
                new_list.append(temp)
    return int(''.join(map(str, new_list)))


