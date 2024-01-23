def narcissistic(value: int) -> (bool, str):
    len_val = len(str(value))
    temp = 0
    for num in str(value):
        temp += int(num) ** len_val

    if temp == value:
        return True, f"{value} is narcissistic"
    else:
        return False, f"{value} is not narcissistic"


print(narcissistic(7), True, '7 is narcissistic');
print(narcissistic(371), True, '371 is narcissistic');

print(narcissistic(122), False, '122 is not narcissistic')
print(narcissistic(4887), False, '4887 is not narcissistic')