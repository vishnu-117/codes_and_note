students_scores = {
    'Alice': {'math': 90, 'science': 80, 'english': 70},
    'Bob': {'math': 70, 'science': 60, 'english': 90},
    'Charlie': {'math': 85, 'science': 90, 'english': 85}
}

def calculate_avg(data):
    return sum(data.values()) / len(data)

result = dict(sorted(students_scores.items(), key=lambda x: calculate_avg(x[1]), reverse=True))
print(result)
