grades = {
    'Alice': 85,
    'Bob': 75,
    'Charlie': 95,
    'David': 60,
    'Eve': 70
}

def find_bright_student(data):
    return data[1] > 80

result = dict(filter(find_bright_student, grades.items()))
print(result)
