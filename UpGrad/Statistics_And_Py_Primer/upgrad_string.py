input_str = input()

d = {}

for i in range(len(input_str)):
    val = input_str[i]
    if val not in d:
        d[val] = 1
    else:
        d[val] += 1


def is_upgrad_str(d: dict) -> bool:
    for i in range(1, len(d) + 1):
        if i not in d.values():
            return False

    return True


print(is_upgrad_str(d))
