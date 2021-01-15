'''
Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
'''

students = []
grades = []
for _ in range(int(input('> Length: '))):
    name = input('>>> Name: ')
    score = float(input('>> Grade: '))
    students.append([name, score])
    grades.append(score)

secondLowest = sorted(list(set(grades)))[1]
print(f'Second lowest grade: {secondLowest}')

for stu_name, stu_score in sorted(students):
    if stu_score == secondLowest:
        print(stu_name)
