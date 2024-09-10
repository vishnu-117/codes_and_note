list_of_dicts = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

result = sorted(list_of_dicts, key= lambda x: x['age'], reverse=True)
print(result)