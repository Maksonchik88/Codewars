def second_symbol(s, symbol):
    if s.count(symbol) <= 1:
        return -1
    elif s.count(symbol) > 1:
        return s.find(symbol, s.find(symbol) + 1)


print(second_symbol('', 'q'))
print(second_symbol('Hello', '!'))
print(second_symbol('Hello world!!!', 'A'))
print(second_symbol('Hello world!!!', 'l'))
