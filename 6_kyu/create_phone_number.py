def create_phone_number(num_list: list[int]) -> str:
    """Creating a phone number."""
    return "(" + "".join(map(str, num_list[0:3])) + ")" + " " + "".join(map(str, num_list[3:6])) + "-" + "".join(map(str, num_list[6:]))


