 # grading program

student_scores = {}

count = int(input("How many student's data you want to enter? "))

for i in range(count):
    key = input("Enter student name: ")
    value = int(input("Enter student's grades: "))
    student_scores[key] = value

print(student_scores)
# print(type(student_scores['Raman']))

student_grades = {}

for student in student_scores:
    if student_scores[student] > 90 and student_scores[student] <= 100:
        student_grades[student] = "Outstanding"
    elif student_scores[student] > 80 and student_scores[student] <= 90 :
        student_grades[student] = "Exceeds Expections"
    elif student_scores[student] > 70 and student_scores[student] <= 80 :
        student_grades[student] = "Accpetable"
    else:
        student_grades[student] = "Fail"

print(student_grades)