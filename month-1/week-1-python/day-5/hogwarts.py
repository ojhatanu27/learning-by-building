#list
students = ["Hermione","Harry","Ron"]
print(students[0])
print(students[1])
print(students[2])

#
for student in students:
    print(student)
#length function
for i in range (len(students)):
    print(i+1,students[i])
#dict(key- value pairs)

students=["Hermione","Harry","Ron","Draco"]
houses=["Gryffindor","Gryffindor","Gryffindor","Slytherin"]
students={
    "Hermione":"Gryffindor",
    "Harry":"Gryffindor",
    "Ron":"Gryffindor",
    "Draco":"Slytherin",
}
print(students["Hermione"]) #this will give value associated with this key
for student in students: #it  will iterate through all the keys
    print(student,students[student],sep=",")
#lists of dictionaries
students=[
    {"name": "Hermione", "house": "Gryffindor","patronous":"Otter"},
    {"name":"Hermione","house":"Gryffindor","patronous":"Otter"},
    {"name":"Ron","house":"Gryffindor","patronous":"Jack Russell Terrier"},
    {"name":"Dracpo","house":"Slytherin","patronous":None}
    ]
for student in students:
    print(student["name"],student["house"],student["patronous"],sep=",")