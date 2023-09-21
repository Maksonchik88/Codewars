def solve(s):
    compare_str = 'aeiou'
    total_count = 0
    temp_count = 0
    for symb in s + 'b':
        if symb in compare_str:
            temp_count += 1
        else:
            if total_count < temp_count:
                total_count = temp_count
            temp_count = 0
    return total_count
