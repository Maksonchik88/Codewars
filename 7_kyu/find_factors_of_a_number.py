def factors(x: int) -> list:
    if not is_digit(x):
        return - 1
    else:
        factors_list = []
        for num in range(1, x + 1):
            if x % num == 0:
                factors_list.append(num)
        return sorted(factors_list, reverse=True), f"didn't work for {x}"

def is_digit(el: any) -> bool:
    if isinstance(el, int) and el >= 1:
        return True


print(factors(54))