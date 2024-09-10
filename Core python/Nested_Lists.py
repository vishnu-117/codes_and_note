# for k in range(5):
name = ["vishnu", "prabhu", "mahes", "rajesh"]
score = [11, 15, 10, 9]
# students = [[i, j] for i in name for j in score]
students = list(zip(name, score))
# print(list(students), "\n\n\n")
students.sort(key=lambda marks: marks[1])
print(students)
