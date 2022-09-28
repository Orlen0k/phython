# # Урок 8. Python: от простого к практике. Продолжение
# # Доделать решение задачи: Задача: Создать информационную систему позволяющую работать
# # с сотрудниками некой компании \ студентами вуза \ учениками школы

class student:
    def __int__(self, full_name, group_number, academic_perfomance):
        self.full_name = full_name
        self.group_number = group_number
        self.academic_perfomance = academic_perfomance


    def average_score(self):
        return (sum(self.academic_perfomance) / len(self.academic_perfomance))

    def __str__(self):
        return(self.full_name)

students = []
for i in range(10):
    print(f'студент {i + 1}:')
    full_name = input('имя ')
    group_number = int(input('номер группы '))
    academic_perfomance = list(map(int, input('оценки (через пробел): ').split()))
    students.append(student(full_name, group_number, academic_perfomance))

students_sorted_by_average_score = sorted(students, key=lambda student: student.average_score())
print(*students_sorted_by_average_score, sep='\n')























