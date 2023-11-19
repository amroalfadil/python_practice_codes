students = ["Hermione","Harry","Ron", "Draco"]
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
'''
for i in range(len(students)):
    print(i + 1, students[i])
'''
# now we can assigne dictionaries to have values

#houses = ["Gryffindor","Gryffindor","Gryffindor","Slytherin"]

students = {
            "Hermione" : "Gryffindor", 
            "Harry": "Gryffindor", 
            "Ron": "Gryffindor", 
            "Draco": "Slytherin"
            }
            #dictionaries allows you to use words
'''
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])
'''
# lets make it more dynamic
#iterate only over the key
'''
for student in students:
    print(student)
'''
#if you would like to print both by adding this to print students[student]
'''
for student in students:
    print(student, students[student], sep= ', ')
'''
# what if we have more information about each of the students such as patronus
# you create a list and create 1 dictionary per student
# note we dealing with None value
students = [
{"name":"Hermione","house": "Gryfindor","patronus": "Otter"},
{"name":"Harry","house": "Gryfindor","patronus": "Stag"},
{"name":"Ron","house": "Gryfindor","patronus": "Jack Russell terrier"},
{"name":"Draco","house": "Slytherin","patronus": None}
]

# now i have access to all these data
# you get all the names
for student in students:
    print(student["name"])
# if you would like the houses to be included 
for student in students:
    print(student["name"], student["house"])
# to add petronus
for student in students:
    print(student["name"], student["house"], student["patronus"], sep = ", ")