def get_middle(example_string: str) -> str:
    if len(example_string) % 2 == 0:
        first_part = example_string[:len(example_string) // 2]
        sec_part = example_string[len(example_string)//2:]
        return (first_part[-1] + sec_part[0])
    else:
        return example_string[len(example_string)//2]


print(get_middle('passap'))
print(get_middle('ghjdbcnkdj'))
print(get_middle('protect'))
