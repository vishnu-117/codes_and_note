students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 75},
    {'name': 'Charlie', 'score': 95}
]

# Define a function that increases the score by 5%
def increase_score(student):
    student['score'] = student['score'] * 1.05
    return student

# Use map to apply the increase_score function to each dictionary
updated_students = list(map(increase_score, students))

print(updated_students)
# Output: [{'name': 'Alice', 'score': 89.25}, {'name': 'Bob', 'score': 78.75}, {'name': 'Charlie', 'score': 99.75}]
