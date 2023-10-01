def reverse_it(data):
    if type(data) in (str, int):
        if type(data) is int:
            return int(str(abs(data))[::-1]) * (-1 if data < 0 else 1)
        else:
            return data[::-1]
    elif type(data) is float:
        return float(str(data)[::-1])
    else:
        return data
