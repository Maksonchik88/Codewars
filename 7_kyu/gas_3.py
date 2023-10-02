def crossover(chromosome1: str, chromosome2: str, index: int) -> list:
    new_1 = chromosome1[: index] + chromosome2[index:]
    new_2 = chromosome2[: index] + chromosome1[index:]
    lst = [new_1, new_2]
    return lst

