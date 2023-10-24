import math


def strong_enough(earthquake: list, age: int) -> str:
    shockwave = []
    for lst in earthquake:
        shockwave.append(sum(lst))
    return ('Safe!' if int(exponential_decay(age)) - math.prod(shockwave) >= 0 else 'Needs Reinforcement!')


def exponential_decay(percent: int) -> int:
    constanta = 1000
    while percent != 0:
        constanta = constanta - ((1 * constanta) / 100)
        percent -= 1
    return constanta


print(strong_enough([[5, 8, 7], [1, 1, 1], [6, 6, 1]], 25))
