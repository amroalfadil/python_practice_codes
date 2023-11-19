students = ["Hermione","Harry","Ron"]
'''
print(students[0])
print(students[1])
print(students[2])
'''
#better way can be done by iteration
'''
for student in students:
    print(student)
'''
# i would like to ierated through the indexes by using the function len() inside range()
'''
    i in range(len(students)):
    print(students[i])
'''
#lets print with the index , maybe add 1 to start from 1
for i in range(len(students)):
    print(i + 1, students[i])