users = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 35, 'city': 'San Francisco'},
    {'name': 'Charlie', 'age': 30, 'city': 'Los Angeles'},
    {'name': 'David', 'age': 40, 'city': 'Chicago'}
]

def filter_based_on_age(data):
    """
    Filter user whose age is more than 30
    """
    return data['age'] > 30

result = list(filter(filter_based_on_age, users))
print(result)