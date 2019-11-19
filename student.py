students = open("student.txt", "r")
key = open("key.txt", "r")

answer = []

for i in key:
    answer = i.split()[1:]

marks = {}

for student in students:
    student =student.split()
    studentName = student[0]
    marks[studentName] = 0

    student = student[1:]
    i = 0
    for option in student:
        if(option == answer[i]):
            marks[studentName] += 1
        i += 1

print(marks)

max = 0
maxname = ""
for k, v in marks.items():
    if(v > max):
        max = v
        maxname = k

print(maxname, max)

students.close()
key.close()
