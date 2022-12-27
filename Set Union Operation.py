n = int(input())
Eng_students = map(int, input().split())
b = int(input())
Fre_students = map(int, input().split())

students = set(Eng_students)
students.update(Fre_students)

print(len(students))
