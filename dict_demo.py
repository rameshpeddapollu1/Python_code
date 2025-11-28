student = {
    "name": "Abhay ram reddy",
    "age": 21,
    "courses": ["Math", "computer science"],
    "marks": {"maths": 90, "computer science": 95}
}

print(student["name"])
print(student.get("age")) 
print(student["age"])
print(student["courses"])
print(student["courses"][1][1])
print(student["marks"]["computer science"])

for key in student:
    print(key, ":", student[key]) 

for key, value in student.items():
    print(key, ":", value) 

data = {
    "student1": {"name": "Bob", "age": 20},
    "student2": {"name": "Eve", "age": 22}
}

print(data["student1"]["name"])