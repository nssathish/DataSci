inp = input()
# ){[[]]}())()
#
# [](){[]()(){}}


def is_balanced(brackets):
    bucket = []

    for bracket in brackets:
        if len(bucket) > 0 and (
            (bucket[-1] == "(" and bracket == ")")
            or (bucket[-1] == "[" and bracket == "]")
            or (bucket[-1] == "{" and bracket == "}")
        ):
            bucket.pop()
        else:
            bucket.append(bracket)

    return "Yes" if len(bucket) == 0 else "No"


print(is_balanced(inp))

paragraph = ["this is python", "this is data science"]

print([word for sentence in paragraph for word in sentence.split(" ")])
