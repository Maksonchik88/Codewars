def change_str(symbol: str) -> str:
    if symbol == 'A' or 'a':
        return '4'
    elif symbol == 'E' or 'e':
        return '3'
    elif symbol == 'l':
        return '1'


def nerdify(txt: str) -> str:
    return ''.join(list(map(change_str, txt))




print(nerdify("Fundamentals"))

# test.assert_equals(nerdify("Fundamentals"), "Fund4m3nt41s")
# test.assert_equals(nerdify("Seven"), "S3v3n")
# test.assert_equals(nerdify("Los Angeles"), "Los 4ng313s")
# test.assert_equals(nerdify("Seoijselawuue"), "S3oijs314wuu3")