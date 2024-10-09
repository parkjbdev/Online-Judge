len = int(input())
students = []
for i in range(len):
    inputs = input().split(" ")
    students.append({"name": inputs[0], "kor": int(inputs[1]), "eng": int(inputs[2]), "math": int(inputs[3])})

students.sort(key=lambda student: (-student["kor"], student["eng"], -student["math"], student["name"]))

for student in students: print(student["name"])