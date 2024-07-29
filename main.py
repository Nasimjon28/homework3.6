grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = ['Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron']
GPA_students=dict()
# students1 = list(students) сначала я пытался изменить множество таким образом, но при выводе список постоянно
#менялся. Я примерно час ломал голову что делать, и решил просто изменить скобки с фигурных на квадратные,
#надеюсь это не является ошибкой задания.
GPA_students.update({students[4]:sum(grades[0])/len(grades[0]),
                     students[1]:sum(grades[1])/len(grades[1]),
                     students[0]:sum(grades[2])/len(grades[2]),
                     students[3]:sum(grades[3])/len(grades[3]),
                     students[2]:sum(grades[4])/len(grades[4])})
print(GPA_students)