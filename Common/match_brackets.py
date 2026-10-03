def isValid(s: str) -> bool:
    stack = []
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        elif len(stack) > 0 and (
            (ch == ")" and (stack[len(stack) - 1] == "("))
            or (ch == "}" and (stack[len(stack) - 1] == "{"))
            or (ch == "]" and (stack[len(stack) - 1] == "["))
        ):
            stack.pop()
        elif len(stack) == 0:
            return False
        else:
            continue

    return len(stack) == 0


s = str(input())
print(isValid(s))
