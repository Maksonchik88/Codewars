def zipvalidate(postcode: str) -> bool:
    if len(postcode) == 6:
        check_str = ''.join(sym for sym in postcode if sym.isdigit())
        if len(check_str) == 6 and int(check_str[0]) not in [0, 5, 7, 8, 9]:
            return True
    return False


print(zipvalidate('198328'))
print(zipvalidate('310003'))
print(zipvalidate('424000'))
print(zipvalidate('12A483'))
print(zipvalidate('1@63'))
print(zipvalidate('111'))
print(zipvalidate('056879'))
print(zipvalidate('1111111'))
