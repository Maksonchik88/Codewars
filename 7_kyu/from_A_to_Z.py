def gimme_the_letters(sp):
    temp_lst = list(map(lambda x: ord(x), sp.split('-')))
    ret_str = ''
    for i in range(temp_lst[0], temp_lst[1] + 1):
        ret_str += chr(i)
    return ret_str


print(gimme_the_letters("a-z"))