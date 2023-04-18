def is_it_a_num(s: str) -> str:
    new_str = ''
    for symbol in s:
        if symbol in '0123456789':
            new_str += str(symbol)
    if len(new_str) == 11 and int(new_str[0]) == 0:
        return new_str
    else:
        return 'Not a phone number'

