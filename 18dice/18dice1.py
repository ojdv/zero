grades = []
while True:
    grade = int(input())
    if grade == -1:
        break
    grades.append(grade)

average = sum(grades) / len(grades)
print("{:.2f}".format(average))