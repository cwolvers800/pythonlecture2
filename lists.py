students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)

print(students[0])
print(students[1])
print(students[2])
#two different ways of doing the same thing

for i in range(len(students)):
    print(i + 1, students[i])