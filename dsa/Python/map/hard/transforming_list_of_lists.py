coordinates = [
    ["1.0", "2.0"],
    ["3.5", "4.1"],
    ["-1.2", "2.3"]
]

def convert_to_tuple(list_data):
    return tuple(map(float, list_data))

result = list(map(convert_to_tuple, coordinates))
print(result)