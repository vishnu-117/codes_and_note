students = {
    'Alice': {'Math': 70, 'Science': 80},
    'Bob': {'Math': 55, 'Science': 65},
    'Charlie': {'Math': 95, 'Science': 90},
    'David': {'Math': 45, 'Science': 50}
}

def filter_all_score_above_60(record):
    return all(score > 60 for score in record.values())

result = {name: subject for name, subject in filter(lambda x: filter_all_score_above_60(x[1]), students.items())}

print(result)
