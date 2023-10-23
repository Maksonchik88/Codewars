def spin_around(lst: list) -> int:
    counter = 0
    for side in lst:
        if side is 'right':
            counter += 90
        elif side is 'left':
            counter -= 90
    return int(abs(counter) / 360)
