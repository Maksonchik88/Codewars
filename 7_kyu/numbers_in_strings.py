def is_digit(st: list) -> list:
    lst = []
    for el in st:
        if el.isdigit():
            lst.append(int(el))
        else:
            continue
    return lst


def solve(num_in_strings: str) -> int:
    str = ''
    for sym in num_in_strings:
        if sym.isdigit():
            str += sym
        else:
            str += '-'
    return max(is_digit(str.split('-')))
