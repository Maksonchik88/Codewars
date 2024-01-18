def solution(s):
    s1 = ''
    for i in s:
        if i.islower():
            s1 += i
        elif i.isupper():
            s1 += ' '
            s1 += i
    return s1

print(solution("helloWorld"))
print(solution("camelCase"))
print(solution("breakCamelCase"))