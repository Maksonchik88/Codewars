def longest(st):
    example = st[0]
    temp_st = st[1:] + ' '
    temp_string = example + ''
    res_dict = {}
    if len(st) <= 1:
        return st
    else:
        for letter in temp_st:
            if example <= letter:
                temp_string += letter
                example = letter
            else:
                res_dict[temp_string] = len(temp_string)
                example = letter
                temp_string = example + ''
    max_val = max(res_dict.values())
    final_dict = {k: v for k, v in res_dict.items() if v == max_val}
    for ek in final_dict.keys():
        return str(ek)

print(longest('asd'), 'as')
print(longest('nab'), 'ab')
print(longest('abcdeapbcdef'), 'abcde')
print(longest('asdfaaaabbbbcttavvfffffdf'), 'aaaabbbbctt')
print(longest('asdfbyfgiklag'), 'fgikl')
print(longest('z'), 'z')
print(longest('zyba'), 'z')