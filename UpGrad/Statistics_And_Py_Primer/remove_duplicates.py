# take input here
from ast import literal_eval

input_list = literal_eval(input())

# remove duplicates from the list
d = {}
for item in input_list:
    if item not in d:
        d[item] = 1

# print the list without duplicates
print(list(d.keys()))
