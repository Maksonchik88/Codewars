def between_extremes(numbers: list) -> int:
    max_num = max(numbers)
    min_mun = min(numbers)
    if len(numbers) >= 2 and max_num == min_mun:
        return 0
    else:
        return len(range(min_mun, max_num))


# def between_extremes(numbers):
#     return max(numbers) - min(numbers)

