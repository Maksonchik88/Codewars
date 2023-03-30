def valid_parentheses(paren_str: str) -> bool:
    if len(paren_str) <= 100:
        a = paren_str.count('(')
        b = paren_str.count(')')
    return True if a == b or len((paren_str)) == 0 else False


print(valid_parentheses("("))
