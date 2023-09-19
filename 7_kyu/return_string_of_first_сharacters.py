def make_string(s: str) -> str:
    temp = s.split()
    return_str = ''
    for word in temp:
        return_str += word[0]
    return return_str

print(make_string("sees eyes xray yoat"))