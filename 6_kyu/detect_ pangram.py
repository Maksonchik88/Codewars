def is_pangram(s: str) -> bool:
    alphabet = [chr(i) for i in range(97, 123)]
    abc_list = sorted(set((el.lower() for el in s if el.isalpha())))
    return True if alphabet == abc_list else False


print(is_pangram("The quick, brown fox jumps over the lazy dog!"), True)
print(is_pangram("1bcdefghijklmnopqrstuvwxyz"), False)