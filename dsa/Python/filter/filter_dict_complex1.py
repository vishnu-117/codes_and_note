employees = [
    {'name': 'Alice', 'projects': {'Project1': 35, 'Project2': 20}},
    {'name': 'Bob', 'projects': {'Project1': 45, 'Project2': 50}},
    {'name': 'Charlie', 'projects': {'Project1': 30, 'Project2': 10}},
    {'name': 'David', 'projects': {'Project1': 20, 'Project2': 40}}
]

def filter_based_on_project_hours(data):
    """
    Filter user whose all project hours is less than 4o
    """
    return all(hours < 40 for hours in data['projects'].values())

result = list(filter(filter_based_on_project_hours, employees))
print(result)