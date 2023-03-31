def trim(phrase, size):
    if len(phrase) <= size:
        return phrase
    if len(phrase) > size:
        if size <= 3:
            return phrase[:size] + "..."
        else:
            return phrase[:size - 3] + "..."


print(trim("gRvNb UQINc nkuc EfcM", 3))
