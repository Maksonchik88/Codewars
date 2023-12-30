def solution(n: int) -> str:
    unique_roman_numbers = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                 'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    roman_str = ''
    for letter, value in unique_roman_numbers.items():
        while n >= value:
            roman_str += letter
            n -= value
    return roman_str


print(solution(1))
print(solution(4))
print(solution(6))
print(solution(14))
print(solution(21))
