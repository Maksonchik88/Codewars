def sum_even_numbers(seq):
    total = sum(filter(lambda x: x % 2 == 0, seq))
    return total



print(sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))