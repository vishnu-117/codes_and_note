nested_list = [
    [2, 'two'],
    [1, 'one'],
    [3, 'three']
]

result = sorted(nested_list, key=lambda x: x[1])
print(result)