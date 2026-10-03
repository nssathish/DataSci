# string = sys.stdin.readline()  # input string

strings = [
    "The tree stands tall.",
    "There are a lot of trees in the forest.",
    "The boy is heading for the school.",
    "It's really hot outside!",
]

# import the regular expression module
import re

# regex pattern
pattern = "trees?"  # write regex here

# check whether pattern is present in string or not
for string in strings:
    result = re.search(pattern, string)  # pass the arguments to the re.search function

    # evaluate result - don't change the following piece of code, it is used to evaluate your regex
    if result != None:
        print(True)
    else:
        print(False)


pattern = "\\d"
replacement = "X"
string = "My address is 13B, Baker Street"
print(re.sub(pattern, replacement, string))


string = "Building careers of tomorrow"
# regex pattern
pattern = "^."  # write a regex that detects the first character of a string
# replacement string
replacement = "$"  # write the replacement string
# check whether pattern is present in string or not
result = re.sub(pattern, replacement, string)  # pass the parameters to the sub function
print(result[0] == "$", result)


string = "Do not compare apples with oranges. Compare apples with apples"
pattern = "[A-z]{5,}"
for match in re.finditer(pattern, string):
    if len(match.group()) >= 5:
        print(match.group())
    else:
        continue

print(re.findall(pattern, string))

string = "Playing outdoor games when its raining outside is always fun!"
pattern = "(ing)"
print(re.findall(pattern, string))
