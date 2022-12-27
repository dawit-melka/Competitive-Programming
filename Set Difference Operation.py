n_Eng = int(input())
Eng_students = map(int, input().split())
n_Fre = int(input())
Fre_students = map(int, input().split())
Eng_students_set = set(Eng_students)

for student in Fre_students:
    if student in Eng_students_set:
        Eng_students_set.remove(student)

print(len(Eng_students_set))
