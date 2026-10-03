from ast import literal_eval

input_list = literal_eval(input())
values = input_list[0]
input_number = input_list[1]
average = sum(values) / len(values)

print(input_number > average)
