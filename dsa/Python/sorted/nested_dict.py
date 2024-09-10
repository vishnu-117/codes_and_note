nested_dict = {
    'item1': {'price': 10, 'quantity': 5},
    'item2': {'price': 15, 'quantity': 2},
    'item3': {'price': 12, 'quantity': 8}
}

result = sorted(nested_dict.items(), key=lambda x: x[1]['price'])
print(result)