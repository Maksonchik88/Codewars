def dad_filter(string):
    string = string.strip().split(',')
    temp_lst = []
    for el in string:
        if el == '' or el == ' ':
            continue
        else:
            el = el.strip()
            temp_lst.append(el)
    return ', '.join(temp_lst)
