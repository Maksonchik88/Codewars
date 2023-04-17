from operator import mul, add, floordiv, sub


def calculator(txt: str) -> str:
    bs = txt.find(' ')
    str1 = txt[: bs]
    bs1 = txt.rfind(' ')
    str2 = txt[bs1 + 1:]
    if "*" in txt:
        return (mul(len(str1), len(str2)) * '.')
    elif "-" in txt:
        return (sub(len(str1), len(str2)) * '.')
    elif "+" in txt:
        return (add(len(str1), len(str2)) * '.')
    elif "//" in txt:
        return (floordiv(len(str1), len(str2)) * '.')
    else:
        raise ValueError(" Недопустимый символ")


print(calculator("..... - ..."))
