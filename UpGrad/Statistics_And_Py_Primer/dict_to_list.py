# {"Mobile": ["Redmi", "Samsung", "Realme"],
# "Laptop": ["Dell", "HP"],
# "TV": ["Videocon", "Sony"] }

from ast import literal_eval

input_str = input()
d: dict = literal_eval(input_str)
result = []
for k, v in d.items():
    for element in v:
        result.append(k + "_" + element)

print(result)
